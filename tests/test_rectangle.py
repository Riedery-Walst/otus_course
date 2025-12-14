import pytest

from src.rectangle import Rectangle

@pytest.fixture
def create_object():
    return Rectangle(3, 4)

@pytest.mark.parametrize("a, b", [
    (0, 0),
    (-1, 1)
])
def test_object_non_positive_param(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)

def test_get_area(create_object):
    assert create_object.get_area() == 12

def test_get_perimeter(create_object):
    assert create_object.get_perimeter() == 14