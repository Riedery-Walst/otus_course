import requests
from tests.logger import create_logger


logger = create_logger(__name__)

def http_request(method: str, url: str, expected_status: int = 200, **kwargs) -> requests.Response:
    response = requests.request(method=method, url=url, **kwargs)

    if response.status_code == expected_status:
        logger.info("OK. URL: %s, Code: %d", url, response.status_code)
    else:
        logger.error("ERROR. URL: %s, Code: %d, Body: %s",
                     url, response.status_code, response.text)
        assert False, f"{method.upper()} {url} failed: expected {expected_status}, got {response.status_code}"

    return response

def get(url, expected_status: int = 200, **kwargs):
    return http_request("get", url, expected_status=expected_status, **kwargs)

def post(url, expected_status: int = 200, **kwargs):
    return http_request("post", url, expected_status=expected_status, **kwargs)

def put(url, expected_status: int = 200, **kwargs):
    return http_request("put", url, expected_status=expected_status, **kwargs)

def delete(url, expected_status: int = 200, **kwargs):
    return http_request("delete", url, expected_status=expected_status, **kwargs)
