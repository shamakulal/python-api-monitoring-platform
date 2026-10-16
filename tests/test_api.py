from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "Python API Monitoring Platform"
    assert data["version"] == "1.0.0"
    assert data["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_services():
    response = client.get("/api/services")

    assert response.status_code == 200

    data = response.json()

    assert data["total_services"] == 3
    assert len(data["services"]) == 3


def test_get_service_by_id():
    response = client.get("/api/services/1")

    assert response.status_code == 200
    assert response.json()["name"] == "user-service"


def test_service_not_found():
    response = client.get("/api/services/999")

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "Service with ID 999 was not found"
    )


def test_summary_endpoint():
    response = client.get("/api/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total_services"] == 3
    assert data["healthy_services"] == 2
    assert data["unhealthy_services"] == 1