# SHELDRA API

Install with `pip install -r requirements-dev.txt`, then start with:

```sh
python -m uvicorn app.main:app --reload
```

The HTTP health check is `GET /health`, the chat entry point is `POST /api/v1/sheldra/chat`, and the streaming endpoint is `WS /ws`.

Create Kafka topics after Compose starts:

```sh
PYTHONPATH=. python scripts/create_topics.py
```
