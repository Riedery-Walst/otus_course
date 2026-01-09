import pytest

from tests.base_service import get


BASE_URL = "https://dog.ceo/api"

@pytest.fixture(scope="session")
def get_all_dog_breeds_list():
    response = get(f"{BASE_URL}/breeds/list/all")

    data = response.json()

    assert len(data["message"]) > 0
    return data

def test_get_random_dog_image():
    response = get(f"{BASE_URL}/breeds/image/random")

    data = response.json()

    assert "status" in data and data["status"] == "success"
    assert "message" in data

@pytest.mark.parametrize("breed, expected_first_image" , [
    ("hound", "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg"),
    ("akita", "https://images.dog.ceo/breeds/akita/512px-Ainu-Dog.jpg")
])
def test_get_images_by_dog_breed(breed, expected_first_image):
    response = get(f"{BASE_URL}/breed/{breed}/images")

    data = response.json()

    assert "status" in data and data["status"] == "success"
    assert "message" in data
    assert data["message"][0] == expected_first_image

def test_get_dog_sub_breeds_list(get_all_dog_breeds_list):
    all_breeds = get_all_dog_breeds_list.get("message")
    for breed, expected_sub_breeds in all_breeds.items():
        response = get(f"{BASE_URL}/breed/{breed}/list")
        assert set(response.json().get("message")) == set(expected_sub_breeds)

        data = response.json()

        assert "status" in data and data["status"] == "success"
        assert "message" in data

@pytest.mark.parametrize("breed" , [
    "hound",
    "akita"
])
def test_get_random_dog_image_by_breed(breed):
    response = get(f"{BASE_URL}/breed/{breed}/images/random")

    data = response.json()

    assert "status" in data and data["status"] == "success"
    assert "message" in data
    assert data["message"].endswith(".jpg")
    assert breed in data["message"]