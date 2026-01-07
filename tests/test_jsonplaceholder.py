import pytest
import requests

from tests.base_service import get, post, put

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_status_code():
    response = get(f"{BASE_URL}/posts")

    assert len(response.json()) > 0

def test_get_post_by_id():
    response = get(f"{BASE_URL}/posts/1")
    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data

@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_post(post_id):
    response = get(f"{BASE_URL}/posts/{post_id}")

    assert response.json()["id"] == post_id

@pytest.mark.parametrize("user_id, expected_count", [
    (1, 10),
    (2, 10),
])
def test_get_posts_by_user(user_id, expected_count):
    response = get(
        f"{BASE_URL}/posts",
        params={"userId": user_id}
    )

    assert len(response.json()) == expected_count

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = post(f"{BASE_URL}/posts", expected_status=201, json=payload)
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_updated_post():
    payload = {
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = put(f"{BASE_URL}/posts/1", json=payload)

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]