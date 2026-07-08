CI Pipeline
===========

Triggers
--------
- `push` on `main`
- `pull_request` targeting `main`

Stages
------
1. `lint` — Black and Ruff (fail on formatting/linting errors)
2. `test` — Run `pytest` with coverage; `--cov-fail-under=70`
3. `security` — Bandit, pip-audit, GitLeaks

Policy
------
- CI must be green before merging to `main`.
- CD (Cloud Run) will be configured in a separate workflow after CI is stable and secrets are set.

Notes
-----
- `pip-audit` is configured to fail on vulnerabilities by default (`--exit-code 1`). Adjust policy if you prefer warnings.
- `gitleaks` action runs repository-level secret detection during CI.
