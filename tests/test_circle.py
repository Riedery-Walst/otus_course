import pytest

from circle import Circle
from figure import Figure


@pytest.fixture
def circles():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    return c1, c2, c3

@pytest.mark.parametrize("a", [
    0,
    -1
])
def test_object_non_positive_param(a):
    with pytest.raises(ValueError):
        Circle(-5)

@pytest.mark.parametrize("radius, expected_area", [
    (3, 28)
])
def test_get_area(radius, expected_area):
    circle = Circle(radius)
    assert circle.get_area() == expected_area

@pytest.mark.parametrize("radius, expected_perimeter", [
    (3, 19)
])
def test_get_perimeter(radius, expected_perimeter):
    circle = Circle(radius)
    assert circle.get_perimeter() == expected_perimeter

def test_add_area(circles):
    c1, c2, c3 = circles

    expected = c1.get_area() + c2.get_area()
    result = c1.add_area(c2)
    assert result == expected

    expected = c1.get_area() + c2.get_area() + c3.get_area()
    result = c1.add_area(c2, c3)
    assert result == expected

    assert isinstance(c1, Figure)
