import pytest

from tests.base_service import get


BASE_URL = "https://dog.ceo/api"

@pytest.fixture(scope="session")
def get_all_dog_breeds_list():
    response = get(f"{BASE_URL}/breeds/list/all")
    return response.json()

def test_get_random_dog_image():
    response = get(f"{BASE_URL}/breeds/image/random")

    data = response.json()

    assert "status" in data and data["status"] == "success"
    assert "message" in data

@pytest.mark.parametrize("breed, expected_status_code, expected_status_message" , [
    ("invalidbreed", 404, "error"),
    ("hound", 200, "success")
])
def test_get_images_by_dog_breed(breed, expected_status_code, expected_status_message):
    response = get(f"{BASE_URL}/breed/{breed}/images", expected_status=expected_status_code)

    data = response.json()

    assert "status" in data and data["status"] == expected_status_message
    assert "message" in data

def test_get_dog_sub_breeds_list(get_all_dog_breeds_list):
    all_breeds = get_all_dog_breeds_list.get("message")
    for breed, expected_sub_breeds in all_breeds.items():
        response = get(f"{BASE_URL}/breed/{breed}/list")
        assert set(response.json().get("message")) == set(expected_sub_breeds)

        data = response.json()

        assert "status" in data and data["status"] == "success"
        assert "message" in data

@pytest.mark.parametrize("breed, expected_status_code, expected_status_message" , [
    ("invalidbreed", 404, "error"),
    ("hound", 200, "success")
])
def test_get_random_dog_image_by_breed(breed, expected_status_code, expected_status_message):
    response = get(f"{BASE_URL}/breed/{breed}/images/random", expected_status=expected_status_code)

    data = response.json()

    assert "status" in data and data["status"] == expected_status_message
    assert "message" in data