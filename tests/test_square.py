import pytest

from figure import Figure
from square import Square

@pytest.fixture
def squares():
    s1 = Square(1)
    s2 = Square(2)
    s3 = Square(3)
    return s1, s2, s3

@pytest.mark.parametrize("a", [
    0,
    -1
])
def test_object_non_positive_param(a):
    with pytest.raises(ValueError):
        Square(a)

@pytest.mark.parametrize("a, expected_area", [
    (3, 9)
])
def test_get_area(a, expected_area):
    square = Square(a)
    assert square.get_area() == expected_area

@pytest.mark.parametrize("a, expected_perimeter", [
    (3, 12)
])
def test_get_perimeter(a, expected_perimeter):
    square = Square(a)
    assert square.get_perimeter() == expected_perimeter

def test_add_area(squares):
    s1, s2, s3 = squares

    expected = s1.get_area() + s2.get_area()
    result = s1.add_area(s2)
    assert result == expected

    expected = s1.get_area() + s2.get_area() + s3.get_area()
    result = s1.add_area(s2, s3)
    assert result == expected

    assert isinstance(s1, Figure)