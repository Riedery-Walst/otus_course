import pytest

from src.triangle import Triangle

@pytest.fixture
def create_object():
    return Triangle(3, 2, 2)

@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),
    (-1, 1, 1),
    (1, 1, 3)
])
def test_init_params(create_object, a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)

def test_get_area(create_object):
    assert create_object.get_area() == 2

def test_get_perimeter(create_object):
    assert create_object.get_perimeter() == 7