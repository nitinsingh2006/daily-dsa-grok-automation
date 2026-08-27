import json
import os
import re
import time
from datetime import date
from pathlib import Path

from openai import OpenAI


COUNT = 20
BATCH_SIZE = 2
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
OUTPUT = Path("solutions") / str(date.today())


def main() -> None:
    key = os.environ.get("XAI_API_KEY")
    if not key:
        raise RuntimeError("Grok API secret is not configured")
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
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict) or not required.issubset(item) or not str(item["solution"]).strip():
            with failed_log.open("a", encoding="utf-8") as log:
                log.write(f"item {index} skipped: missing required fields\n")
            continue
        safe = re.sub(r"[^a-z0-9]+", "-", item["title"].lower()).strip("-")[:60]
        (OUTPUT / f"{index:02d}-{safe or 'problem'}.md").write_text(
            f"# {item['title']}\n\n**Difficulty:** {item['difficulty']}  \n**Topic:** {item['topic']}\n\n{item['problem']}\n\n## Approach\n{item['approach']}\n\n## Complexity\n{item['complexity']}\n\n## Solution\n```python\n{item['solution']}\n```\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
