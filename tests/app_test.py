import pytest
from src.app import app


@pytest.fixture
def client() -> object:
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_upper(client: object) -> None:
    r = client.post("/format", json={"text": "hello", "style": "upper"})
    assert r.status_code == 200
    assert r.get_json()["result"] == "HELLO"


def test_lower(client: object) -> None:
    r = client.post("/format", json={"text": "WORLD", "style": "lower"})
    assert r.get_json()["result"] == "world"


def test_title(client: object) -> None:
    r = client.post(
        "/format", json={"text": "hello world", "style": "title"}
    )
    assert r.get_json()["result"] == "Hello World"


def test_reverse(client: object) -> None:
    r = client.post("/format", json={"text": "abc", "style": "reverse"})
    assert r.get_json()["result"] == "cba"


def test_unknown_style(client: object) -> None:
    r = client.post(
        "/format", json={"text": "hi", "style": "nonexistent"}
    )
    assert r.status_code == 400
