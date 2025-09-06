from fastapi.testclient import TestClient
from app.main import app
import app.model as model_mod

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "Email Classification API" in r.json().get("message", "")

def test_classify_without_model(monkeypatch):
    monkeypatch.setattr(model_mod, "_model", None)
    r = client.post("/classify", json={"email_text": "Hello"})
    assert r.status_code == 200
    data = r.json()
    assert "predicted_category" in data
    assert "confidence" in data

