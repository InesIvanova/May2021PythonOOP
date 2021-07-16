from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def area(self):
        return self.side * self.h/2

    def perimeter(self):
        return "perimeter"


t = Triangle(5, 6)
print(t)