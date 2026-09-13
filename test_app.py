import pytest

import app as app_module


@pytest.fixture
def client():
    app_module.recent_estimates.clear()
    return app_module.app.test_client()


def test_valid_estimate_returns_200_with_total_and_breakdown(client):
    response = client.post("/estimate", json={"distance_km": 5, "duration_min": 10, "surge": 1.5})
    assert response.status_code == 200
    body = response.get_json()
    assert body["total"] == 195.0
    assert "breakdown" in body


def test_missing_field_is_rejected(client):
    response = client.post("/estimate", json={"distance_km": 5})
    assert response.status_code == 400
    assert "duration_min" in response.get_json()["error"]


def test_wrong_type_is_rejected(client):
    response = client.post("/estimate", json={"distance_km": "five", "duration_min": 10})
    assert response.status_code == 400
    assert "distance_km" in response.get_json()["error"]


def test_no_body_is_rejected(client):
    response = client.post("/estimate")
    assert response.status_code == 400


def test_estimates_endpoint_returns_newest_first(client):
    client.post("/estimate", json={"distance_km": 1, "duration_min": 1})
    client.post("/estimate", json={"distance_km": 2, "duration_min": 2})

    body = client.get("/estimates").get_json()

    assert len(body) == 2
    assert body[0]["breakdown"]["distance_cost"] == 24  # the second, more recent request


def test_estimates_list_caps_at_ten(client):
    for i in range(11):
        client.post("/estimate", json={"distance_km": i, "duration_min": 1})

    body = client.get("/estimates").get_json()

    assert len(body) == 10
    assert body[0]["breakdown"]["distance_cost"] == 120  # the 11th request (i=10), newest first
