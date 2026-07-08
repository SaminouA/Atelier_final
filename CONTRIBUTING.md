# Contributing

## Workflow

1. Create a feature branch from `main`.
2. Make your changes and add tests when relevant.
3. Run the local checks before opening a pull request.
4. Open a pull request with a clear description and link the relevant issue if needed.

## Local checks

```bash
python -m pip install -r requirements-dev.txt
pytest -q
black --check .
ruff .
```
