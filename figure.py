from abc import abstractmethod, ABC

from util import get_round, check_parameters


class Figure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @get_round
    def add_area(self, *args):
        total = 0
        for arg in args:
            if not isinstance(arg, Figure):
                raise ValueError("Argument is not instance of Figure")
            total += arg.get_area()
        return self.get_area() + total