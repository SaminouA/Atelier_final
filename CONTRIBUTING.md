# Contribuer

## Branches

Travaillez sur une branche courte nommee selon le besoin, puis ouvrez une Pull Request
vers `main`.

## Commits

Utilisez Conventional Commits :

- `feat: ...`
- `fix: ...`
- `test: ...`
- `chore: ...`
- `docs: ...`

## Verification locale

```bash
black --check .
ruff check .
pytest --cov=src --cov-report=xml --cov-fail-under=70
bandit -r src
pip-audit -r requirements.txt
```
