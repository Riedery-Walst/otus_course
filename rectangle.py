from figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a + self.b

    def get_perimeter(self):
        return self.a * self.b