"""Tests for the document/tag API.

The first three pass out of the box. `test_add_tag` is skipped — un-skip it
and make it pass as part of your solution (acceptance criterion #7).
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.seed import seed


@pytest.fixture(autouse=True)
def fresh_db():
    seed()          # rebuild the database before every test
    yield


client = TestClient(app)


def test_list_documents():
    r = client.get("/api/documents")
    assert r.status_code == 200
    assert len(r.json()) > 0


def test_get_document_includes_tags():
    r = client.get("/api/documents/1")
    assert r.status_code == 200
    assert isinstance(r.json().get("tags"), list)


def test_get_missing_document_returns_404():
    assert client.get("/api/documents/99999").status_code == 404


@pytest.mark.skip(reason="TODO: implement add_tag, then remove this skip line")
def test_add_tag():
    before = len(client.get("/api/documents/1").json()["tags"])
    r = client.post("/api/documents/1/tags", json={"type": "party", "value": "Acme Corp"})
    assert r.status_code == 201
    after = len(client.get("/api/documents/1").json()["tags"])
    assert after == before + 1
