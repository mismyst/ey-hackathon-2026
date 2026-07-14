from fastapi.testclient import TestClient

from app.main import app


def test_health() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_returns_contract() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/sheldra/chat", json={"worker_id": "worker-1", "message": "Help"}
        )
    assert response.status_code == 200
    assert response.json()["trace_id"]
