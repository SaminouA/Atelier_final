# todo-api-nadira-kevin

API Flask simple pour gérer une liste de tâches en mémoire.

## Fonctionnalités

- `GET /` : informations sur l'application
- `GET /health` : vérification de santé
- `GET /version` : version de l'application
- `GET /tasks` : lister les tâches
- `POST /tasks` : créer une tâche

## Installation locale

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements-dev.txt
```

## Exécution

```bash
python -m src.app
```

L'application écoute ensuite sur `http://127.0.0.1:8000`.

## Tests

```bash
pytest -q
```

## Docker

```bash
docker compose up --build
```

## CI/CD

Le projet contient un workflow GitHub Actions pour :
- Black
- Ruff
- pytest avec couverture
- Bandit
- pip-audit
- GitLeaks
