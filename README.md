# todo-api-nadira-kevin

API Flask simple pour gerer une liste de taches en memoire.

## Fonctionnalites

- `GET /` : informations sur l'application
- `GET /health` : verification de sante
- `GET /version` : version de l'application
- `GET /tasks` : lister les taches
- `POST /tasks` : creer une tache

## Ressources

- Depot GitHub : `todo-api-nadira-kevin`
- Service Cloud Run : `todo-api-nadira-kevin`
- Depot Artifact Registry : `todo-repo-nadira-kevin`
- Projet GCP : `tp9-demo-2026`
- Region : `europe-west1`

## Installation locale

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements-dev.txt
```

## Execution

```bash
python -m src.app
```

L'application ecoute ensuite sur `http://127.0.0.1:8080`.

## Tests

```bash
pytest --cov=src --cov-report=xml --cov-fail-under=70
```

## Docker

```bash
docker compose up --build
```

## CI/CD

Le projet contient des workflows GitHub Actions pour :

- Black
- Ruff
- pytest avec couverture
- Bandit
- pip-audit
- GitLeaks
- build et push Docker vers Artifact Registry
- deploiement Cloud Run

## Deploiement Cloud Run

Le workflow de deploiement automatique est defini dans `.github/workflows/cd.yml`.
Il publie l'image Docker dans Artifact Registry puis deploie l'application sur Cloud Run
quand la CI reussit sur `main`.

Secret GitHub requis :

- `GCP_SA_KEY` : contenu JSON de la cle du service account `github-deployeur@tp9-demo-2026.iam.gserviceaccount.com`

## Releases

La gestion des releases est preparee avec Release Please via `.github/workflows/release-please.yml`.
