import json

import pytest
import requests
from jsondiff import diff

from tests.logger import create_logger

logger = create_logger()

DATA_PATH = "data/"
ALL_DOG_BREADS_JSON = DATA_PATH + "all_dog_breads.json"

@pytest.fixture
def load_all_dog_bread():
    with open(ALL_DOG_BREADS_JSON, "r") as f:
       return json.load(f)

def test_get_random_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    assert response.json().get("status") == "success"

def test_get_all_dog_breads(load_all_dog_bread):
    expected = load_all_dog_bread
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    assert diff(response, expected)

