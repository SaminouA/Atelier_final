# Mon projet

Application Flask minimale avec tests, configuration qualité et support Docker.

## Installation locale

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Lancer l'application

```bash
python -m src.app
```

L'application écoute sur `http://127.0.0.1:8000`.

## Tests et qualité

```bash
pytest
ruff check .
black --check .
```

## Docker

```bash
docker compose up --build
```

Le healthcheck vérifie l'endpoint `/health`.
