import pytest

from figure import Figure
from rectangle import Rectangle


@pytest.fixture
def rectangles():
    r1 = Rectangle(2, 3)
    r2 = Rectangle(4, 5)
    r3 = Rectangle(1, 1)
    return r1, r2, r3

@pytest.mark.parametrize("a, b", [
    (0, 0),
    (-1, 1)
])
def test_object_non_positive_param(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)

@pytest.mark.parametrize("a, b, expected_area", [
    (3, 4, 12),
])
def test_get_area(a, b, expected_area):
    rectangle = Rectangle(a, b)
    assert rectangle.get_area() == expected_area

@pytest.mark.parametrize("a, b, expected_perimeter", [
    (3, 4, 14),
])
def test_get_perimeter(a, b, expected_perimeter):
    rectangle = Rectangle(a, b)
    assert rectangle.get_perimeter() == expected_perimeter

def test_add_area(rectangles):
    r1, r2, r3 = rectangles

    expected = r1.get_area() + r2.get_area()
    result = r1.add_area(r2)
    assert result == expected

    expected = r1.get_area() + r2.get_area() + r3.get_area()
    result = r1.add_area(r2, r3)
    assert result == expected

    assert isinstance(r1, Figure)