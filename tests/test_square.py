import pytest

from src.figure import Figure
from src.square import Square

@pytest.fixture
def create_object():
    return Square(3)

def object_is_instance_of_parent(create_object):
    assert isinstance(create_object, Figure)

@pytest.mark.parametrize("a", [0, -1])
def test_object_non_positive_param(a):
    with pytest.raises(ValueError):
        Square(a)

def test_get_area(create_object):
    assert create_object.get_area() == 9

def test_get_perimeter(create_object):
    assert create_object.get_perimeter() == 12