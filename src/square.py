from figure import Figure
from util import check_parameters, get_round


class Square(Figure):
    @check_parameters
    def __init__(self, a: int | float):
        self.a = a

    @get_round
    def get_area(self):
        return self.a * self.a

    @get_round
    def get_perimeter(self):
        return self.a * 4