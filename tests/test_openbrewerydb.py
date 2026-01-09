import pytest

from models.brewery import Brewery
from tests.base_service import get


BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

@pytest.fixture(scope="session")
def brewery_id():
    response = get(BASE_URL)

    breweries = response.json()
    assert len(breweries) > 0

    return breweries[0]["id"]

def test_get_brewery_by_id(brewery_id):
    response = get(f"{BASE_URL}/{brewery_id}")

    brewery = Brewery.model_validate(response.json())
    assert brewery.id == brewery_id

@pytest.mark.parametrize("city", [
    "Portland",
    "San Diego",
    "Chicago",
])
def test_get_breweries_by_city(city):
    response = get(BASE_URL, params={"by_city": city})

    data = response.json()

    assert len(data) > 0

    for brewery in data:
        assert city.lower() in brewery["city"].lower()

def test_get_random_different_brewery():
    ids = set()

    for _ in range(10):
        response = get(f"{BASE_URL}/random")
        data = response.json()

        brewery = Brewery.model_validate(data[0])
        ids.add(brewery.id)

    assert len(ids) > 1

@pytest.mark.parametrize("params, expected_len", [
    ({}, 1),
    ({"size": 5}, 5),
    ({"size": 10}, 10),
])
def test_get_random_brewery_with_size(params, expected_len):
    response = get(f"{BASE_URL}/random", params=params)

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == expected_len

@pytest.mark.parametrize("query, page, first_brewery_name, per_page, expected_length", [
    ("san%diego", 1, "G8 Development, Inc.", 3, 3),
    ("new%york", 2, "Council Rock Brewery", None, 50),
    ("washington", None, "Haywire Brewing Company", 200, 200)
])
def test_search_breweries(query, page, first_brewery_name, per_page, expected_length):
    params = {
        "query": query,
        "page": page,
        "per_page": per_page
    }

    response = get(f"{BASE_URL}/search?", params=params)

    data = response.json()
    for brewery in data:
        Brewery.model_validate(brewery)
    assert len(data) == expected_length
    assert data[0]["name"] == first_brewery_name

