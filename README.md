# Daily DSA Grok Automation

Generates 30 DSA solutions each day with the xAI API, validates the response shape, and commits the results from GitHub Actions. The workflow runs in the cloud, so the local PC can be shut down.

## Required repository secrets

- `XAI_API_KEY`

The workflow has a daily UTC schedule and can also be started manually. Generated files are written under `solutions/YYYY-MM-DD/`.
