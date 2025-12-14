import pytest

from src.figure import Figure
from src.triangle import Triangle

@pytest.fixture
def create_object():
    return Triangle(3, 2, 2)

def object_is_instance_of_parent(create_object):
    assert isinstance(create_object, Figure)

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