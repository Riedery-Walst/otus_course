from tests.base_service import get


def test_url_status_code(url, status_code):
    response = get(url)

    assert response.status_code == int(status_code)