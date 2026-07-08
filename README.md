# todo-api-nadira-kevin

[![CI](https://github.com/SaminouA/Atelier_final/actions/workflows/ci.yml/badge.svg)](https://github.com/SaminouA/Atelier_final/actions/workflows/ci.yml)
[![Docs](https://github.com/SaminouA/Atelier_final/actions/workflows/pages.yml/badge.svg)](https://github.com/SaminouA/Atelier_final/actions/workflows/pages.yml)
[![Release Please](https://github.com/SaminouA/Atelier_final/actions/workflows/release-please.yml/badge.svg)](https://github.com/SaminouA/Atelier_final/actions/workflows/release-please.yml)

API Flask de gestion de taches pour l'atelier final DevOps.

## Ressources

- Depot GitHub : `todo-api-nadira-kevin`
- Service Cloud Run : `todo-api-nadira-kevin`
- Depot Artifact Registry : `todo-repo-nadira-kevin`
- Projet GCP : `atelier-final-2026`
- Region : `europe-west1`

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
pytest --cov=src --cov-report=xml --cov-fail-under=70
bandit -r src
pip-audit -r requirements.txt
```

## Docker

```bash
docker compose up --build
```

## Deploiement Cloud Run

Le workflow CI/CD deploie automatiquement sur Cloud Run apres un push sur `main`
si la CI est verte et si les secrets GitHub suivants sont configures :

- `GCP_WORKLOAD_IDENTITY_PROVIDER`
- `GCP_SERVICE_ACCOUNT`

L'image est publiee dans Artifact Registry avec le tag SemVer `v1.0.0` et le SHA
du commit.

## Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT, voir [LICENSE](LICENSE).
