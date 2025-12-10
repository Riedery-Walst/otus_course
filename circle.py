import math

from figure import Figure
from util import check_parameters, get_round


class Circle(Figure):
    @check_parameters
    def __init__(self, r: int | float):
        self.r = r

    @get_round
    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    @get_round
    def get_perimeter(self):
        return 2 * math.pi * self.r