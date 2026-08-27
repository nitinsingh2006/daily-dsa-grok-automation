import json
import os
import re
from datetime import date
from pathlib import Path

from openai import OpenAI


COUNT = 20
BATCH_SIZE = 5
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
OUTPUT = Path("solutions") / str(date.today())


def main() -> None:
    key = os.environ.get("XAI_API_KEY")
    if not key:
        raise RuntimeError("Grok API secret is not configured")
    client = OpenAI(api_key=key, base_url="https://api.groq.com/openai/v1")
    all_items = []
    for batch_start in range(0, COUNT, BATCH_SIZE):
        batch_count = min(BATCH_SIZE, COUNT - batch_start)
        prompt = f"""Create exactly {batch_count} original DSA practice problems with correct solutions.
Return ONLY a JSON object with a `solutions` array. Each item must have: title, difficulty, topic, problem,
approach, complexity, and compact solution (Python 3 code). Make every title unique,
keep each problem and explanation under 80 words, ensure code is syntactically valid,
and do not use markdown fences."""
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            response_format={"type": "json_object"},
        )
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", (response.choices[0].message.content or "").strip())
        parsed = json.loads(raw)
        items = parsed.get("solutions") if isinstance(parsed, dict) else parsed
        if not isinstance(items, list) or len(items) != batch_count:
            raise ValueError(f"Expected {batch_count} solutions in batch, received invalid output")
        all_items.extend(items)
    items = all_items
    if not isinstance(items, list) or len(items) != COUNT:
        raise ValueError(f"Expected {COUNT} solutions, received {len(items) if isinstance(items, list) else 'invalid JSON'}")
    required = {"title", "difficulty", "topic", "problem", "approach", "complexity", "solution"}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for index, item in enumerate(items, 1):
        if not required.issubset(item) or not item["solution"].strip():
            raise ValueError(f"Solution {index} has missing required fields")
        safe = re.sub(r"[^a-z0-9]+", "-", item["title"].lower()).strip("-")[:60]
        (OUTPUT / f"{index:02d}-{safe or 'problem'}.md").write_text(
            f"# {item['title']}\n\n**Difficulty:** {item['difficulty']}  \n**Topic:** {item['topic']}\n\n{item['problem']}\n\n## Approach\n{item['approach']}\n\n## Complexity\n{item['complexity']}\n\n## Solution\n```python\n{item['solution']}\n```\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
