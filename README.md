# SHELDRA

Industrial Safety Intelligence Platform monorepo.

## Start the platform

1. Copy `.env.example` to `.env` and replace the development credentials.
2. Start dependencies: `docker compose up -d`.
3. Start the API: `cd backend && python -m uvicorn app.main:app --reload`.
4. Start the dashboard: `cd frontend && npm install && npm run dev`.

API documentation is available at `http://localhost:8000/docs`; the dashboard runs at `http://localhost:3000`.

## Repository layout

- `backend/` — FastAPI API, WebSocket endpoint, Redis and Kafka adapters.
- `frontend/` — Next.js dashboard foundation.
- `knowledge-graph/` — reserved for the P0-KG implementation.
- `data-generators/` — reserved for the P0-DAT implementation.
