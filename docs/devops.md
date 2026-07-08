# DevOps

## CI

La CI execute Black, Ruff, pytest avec couverture, Bandit, pip-audit et GitLeaks.

## CD

Le workflow de deploiement construit l'image Docker, la pousse dans Artifact Registry,
puis deploie le service Cloud Run `todo-api-nadira-kevin`.

## Releases

`release-please` gere les Pull Requests de release, le changelog et les versions SemVer.
