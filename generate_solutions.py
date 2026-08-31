import json
import os
import re
import subprocess
import time
from datetime import date
from pathlib import Path

from openai import OpenAI


COUNT = 20
BATCH_SIZE = 2
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
OUTPUT = Path("solutions") / str(date.today())
LOCK_FILE = Path("automation.lock")


def main() -> None:
    key = os.environ.get("XAI_API_KEY")
    if not key:
        raise RuntimeError("Grok API secret is not configured")

    # Improvement 3: Verify git identity is configured before doing any work
    git_name = subprocess.run(
        ["git", "config", "user.name"],
        capture_output=True, text=True,
    ).stdout.strip()
    git_email = subprocess.run(
        ["git", "config", "user.email"],
        capture_output=True, text=True,
    ).stdout.strip()
    if not git_name or not git_email:
        raise RuntimeError(
            "Git identity not configured — run:\n"
            "  git config user.name \"Your Name\"\n"
            "  git config user.email \"you@example.com\""
        )

    client = OpenAI(api_key=key, base_url="https://api.groq.com/openai/v1")
    all_items = []
    failed_log = Path("failed_items.log")
    raw_failure_dir = Path("raw_failures")

    def request_batch(batch_count: int, batch_number: int) -> list:
        prompt = f"""Return valid JSON only. Create exactly {batch_count} original DSA practice problems.
The response must be JSON in this exact structure:
{{"solutions": [{{"title": "Two Sum", "difficulty": "Easy", "topic": "Arrays",
"problem": "Find two indices...", "approach": "Use a hash map.",
"complexity": "O(n) time, O(n) space", "solution": "def solve(nums, target): pass"}}]}}
The JSON array must contain EXACTLY {batch_count} objects. Count them before responding.
Every item must have
title, difficulty, topic, problem, approach, complexity, and compact Python 3 solution.
Keep problem and explanation under 80 words, ensure code is syntactically valid, and
do not use markdown fences or any text outside the JSON object."""
        last_error = None
        for attempt in range(1, 3):
            current_prompt = prompt
            if attempt == 2:
                current_prompt += f"\nReturn EXACTLY {batch_count} solutions, no more no less, as a JSON array inside the solutions field."
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": current_prompt}],
                    temperature=0.2,
                    max_tokens=4096,
                    response_format={"type": "json_object"},
                )
                raw = (response.choices[0].message.content or "").strip()
                if not raw:
                    raise ValueError("empty model response")
                raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw).strip()
                parsed = json.loads(raw)
                items = parsed.get("solutions") if isinstance(parsed, dict) else parsed
                if not isinstance(items, list):
                    raise ValueError("solutions field was not a list")
                if len(items) >= batch_count:
                    return items[:batch_count]
                if attempt == 2:
                    missing = batch_count - len(items)
                    with failed_log.open("a", encoding="utf-8") as log:
                        log.write(f"batch {batch_number}: {missing} item(s) missing after retry\n")
                    return items
                raise ValueError(f"expected {batch_count} solutions, received {len(items)}")
            except Exception as error:
                last_error = error
                if 'raw' in locals() and raw:
                    raw_failure_dir.mkdir(parents=True, exist_ok=True)
                    (raw_failure_dir / f"batch_{batch_number}.json").write_text(raw, encoding="utf-8")
                if attempt < 2:
                    time.sleep(2)
        with failed_log.open("a", encoding="utf-8") as log:
            log.write(f"batch {batch_number} failed: {last_error}\n")
        return []

    for batch_start in range(0, COUNT, BATCH_SIZE):
        batch_count = min(BATCH_SIZE, COUNT - batch_start)
        all_items.extend(request_batch(batch_count, batch_start // BATCH_SIZE + 1))
    items = all_items
    required = {"title", "difficulty", "topic", "problem", "approach", "complexity", "solution"}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    committed_count = 0
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict) or not required.issubset(item) or not str(item["solution"]).strip():
            with failed_log.open("a", encoding="utf-8") as log:
                log.write(f"item {index} skipped: missing required fields\n")
            continue
        safe = re.sub(r"[^a-z0-9]+", "-", item["title"].lower()).strip("-")[:60]
        filename = f"{index:02d}-{safe or 'problem'}.md"
        filepath = OUTPUT / filename
        filepath.write_text(
            f"# {item['title']}\n\n**Difficulty:** {item['difficulty']}  \n**Topic:** {item['topic']}\n\n{item['problem']}\n\n## Approach\n{item['approach']}\n\n## Complexity\n{item['complexity']}\n\n## Solution\n```python\n{item['solution']}\n```\n",
            encoding="utf-8",
        )
        # Stage only this file and commit immediately
        try:
            subprocess.run(
                ["git", "add", str(filepath)],
                check=True,
            )
            subprocess.run(
                ["git", "commit", "-m", f"solve: {filename}"],
                check=True,
            )
            committed_count += 1
        except subprocess.CalledProcessError as git_error:
            with failed_log.open("a", encoding="utf-8") as log:
                log.write(f"git commit failed for {filename}: {git_error}\n")

    # Push all commits together in a single push
    if committed_count > 0:
        # Improvement 2: rebase on top of any remote changes before pushing
        # to avoid non-fast-forward rejection errors
        try:
            subprocess.run(["git", "pull", "--rebase"], check=True)
        except subprocess.CalledProcessError as rebase_error:
            with failed_log.open("a", encoding="utf-8") as log:
                log.write(f"git pull --rebase failed: {rebase_error}\n")
        try:
            subprocess.run(["git", "push"], check=True)
        except subprocess.CalledProcessError as push_error:
            with failed_log.open("a", encoding="utf-8") as log:
                log.write(f"git push failed: {push_error}\n")

    # Improvement 1: final summary — compare committed_count against target
    if committed_count == COUNT:
        print(f"✅ All {COUNT} solutions committed and pushed.")
    else:
        warning = (
            f"⚠️  Only {committed_count}/{COUNT} solutions committed today"
            " — check failed_items.log"
        )
        print(warning)
        with failed_log.open("a", encoding="utf-8") as log:
            log.write(f"SUMMARY: {warning}\n")


if __name__ == "__main__":
    if LOCK_FILE.exists():
        print("⚠️ Another run already in progress (lock file exists) — exiting")
    else:
        LOCK_FILE.touch()
        try:
            main()
        finally:
            LOCK_FILE.unlink(missing_ok=True)
