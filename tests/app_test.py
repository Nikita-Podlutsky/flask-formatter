from typing import Generator
import pytest
from flask.testing import FlaskClient
from src.app import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_upper(client: FlaskClient) -> None:
    r = client.post("/format", json={"text": "hello", "style": "upper"})
    assert r.status_code == 200
    assert r.get_json()["result"] == "HELLO"


def test_lower(client: FlaskClient) -> None:
    r = client.post("/format", json={"text": "WORLD", "style": "lower"})
    assert r.get_json()["result"] == "world"


def test_title(client: FlaskClient) -> None:
    r = client.post(
        "/format", json={"text": "hello world", "style": "title"}
    )
    assert r.get_json()["result"] == "Hello World"


def test_reverse(client: FlaskClient) -> None:
    r = client.post("/format", json={"text": "abc", "style": "reverse"})
    assert r.get_json()["result"] == "cba"


def test_unknown_style(client: FlaskClient) -> None:
    r = client.post(
        "/format", json={"text": "hi", "style": "nonexistent"}
    )
    assert r.status_code == 400
