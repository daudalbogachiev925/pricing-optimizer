def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_add_vw(client):
    r = client.post("/api/surveys/vw", json={
        "respondent_id": "r1", "too_cheap": 5, "bargain": 20,
        "expensive": 50, "too_expensive": 80})
    assert r.status_code == 201

def test_vw_analysis(client):
    for i in range(4):
        client.post("/api/surveys/vw", json={
            "respondent_id": f"r{i}", "too_cheap": 5 + i,
            "bargain": 20 + i, "expensive": 50 + i, "too_expensive": 80 + i})
    r = client.get("/api/analysis/vw")
    assert r.status_code == 200
    assert r.json()["n_respondents"] == 4

def test_gg_analysis(client):
    client.post("/api/surveys/gg", json={
        "price": 50, "interested": 100, "total_asked": 200})
    r = client.get("/api/analysis/gg")
    assert r.status_code == 200
