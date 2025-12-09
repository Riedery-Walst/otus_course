from figure import Figure
from util import check_parameters, get_round


class Rectangle(Figure):
    @check_parameters
    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    @get_round
    def get_area(self):
        return self.a + self.b

    @get_round
    def get_perimeter(self):
        return self.a * self.b