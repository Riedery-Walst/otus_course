import math

from figure import Figure


class Circle(Figure):
    def __init__(self, r: int):
        self.r = r

    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.r