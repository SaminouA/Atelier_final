# todo-api-nadira-kevin

API Flask de gestion de taches pour l'atelier final DevOps.

## Installation

```bash
python -m pip install -r requirements-dev.txt
```

## Lancer en local

```bash
python -m src.app
```

L'API ecoute sur `http://127.0.0.1:8080`.

## Routes

- `GET /`
- `GET /health`
- `GET /version`
- `GET /tasks`
- `POST /tasks`

Exemple de creation de tache :

```bash
curl -X POST http://127.0.0.1:8080/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Faire la CI\"}"
```

## Qualite et tests

```bash
black --check .
ruff check .
pytest
bandit -r src
pip-audit -r requirements.txt
```

## Docker

```bash
docker compose up --build
```
