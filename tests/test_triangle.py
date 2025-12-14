import pytest

from figure import Figure
from triangle import Triangle


@pytest.fixture
def triangles():
    t1 = Triangle(3, 4, 5)
    t2 = Triangle(5, 12, 13)
    t3 = Triangle(6, 8, 10)
    return t1, t2, t3

@pytest.mark.parametrize("a, b, c", [
    (0, 0, 0),
    (-1, 1, 1),
    (1, 1, 3)
])
def test_init_params(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)

@pytest.mark.parametrize("a, b, c, expected_area", [
    (3, 2, 2, 2)
])
def test_get_area(a, b, c, expected_area):
    triangle = Triangle(a, b, c)
    assert triangle.get_area() == expected_area

@pytest.mark.parametrize("a, b, c, expected_perimeter", [
    (3, 2, 2, 7)
])
def test_get_perimeter(a, b, c, expected_perimeter):
    triangle = Triangle(a, b, c)
    assert triangle.get_perimeter() == expected_perimeter


def test_add_area(triangles):
    t1, t2, t3 = triangles

    expected = t1.get_area() + t2.get_area()
    result = t1.add_area(t2)
    assert result == expected

    expected = t1.get_area() + t2.get_area() + t3.get_area()
    result = t1.add_area(t2, t3)
    assert result == expected

    assert isinstance(t1, Figure)