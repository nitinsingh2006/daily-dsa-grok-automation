# Daily DSA Grok Automation

Generates 20 DSA solutions each day with the Groq API, validates the response shape, and commits the results from GitHub Actions. The workflow runs in the cloud, so the local PC can be shut down.

## Required repository secrets

- `XAI_API_KEY`

The workflow has a daily UTC schedule and can also be started manually. Generated files are written under `solutions/YYYY-MM-DD/`.

## How it works

GitHub Actions generates, validates, commits, and pushes the daily DSA solutions automatically.

## Output

Each run stores the generated practice files in a date-based folder under `solutions/`.

<!-- Co-author update part 1: timestamp 1788521388.3886352 -->

<!-- Co-author update part 2: timestamp 1788521402.646013 -->
