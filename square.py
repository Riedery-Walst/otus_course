from figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        self.a = a

    def get_area(self):
        return self.a * self.a

    def get_perimeter(self):
        return self.a * 4