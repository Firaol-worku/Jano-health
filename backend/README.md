# Backend Quickstart

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

Use testing settings to run with in-memory SQLite:

```bash
python manage.py test tests --settings=config.settings.testing
```

## Run API locally

```bash
python manage.py migrate
python manage.py runserver
```

Health check endpoint: `GET /health/`
