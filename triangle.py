import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        if not self.check_triangle_exists():
            raise ValueError("Invalid value for triangle")

    def get_area(self):
        half_p = self.get_half_perimeter()
        return math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_half_perimeter(self):
        return self.get_perimeter() / 2

    def check_triangle_exists(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False

        half_p = self.get_half_perimeter()
        return half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c) >= 0