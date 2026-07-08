# API

## Routes

- `GET /` : informations de l'application
- `GET /health` : etat de sante
- `GET /version` : version courante
- `GET /tasks` : liste des taches en memoire
- `POST /tasks` : creation d'une tache

## Exemple

```bash
curl -X POST http://127.0.0.1:8080/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Faire la CI\"}"
```

Les taches sont stockees en memoire. Elles disparaissent au redemarrage.
