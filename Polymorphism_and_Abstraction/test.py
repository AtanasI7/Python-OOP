from idlelib.query import CustomRun
from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Square(Shape):

    def __init__(self, a, b):
        Shape.__init__(self, a, b)

    def calculate_area(self):
        return self.a * 4

    def calculate_perimeter(self):
        return 4 * self.a


class Triangle(Shape):

        def __init__(self, a, b, h):
            Shape.__init__(self, a, b)
            self.h = h

        def calculate_area(self):
            return self.a * self.b * self.h

        def calculate_perimeter(self):
            return self.a + self.b + self.h



# class Rectangle(Shape):
#
#     def __init__(self, height, width):
#         self.__height = height
#         self.__width = width
#
#     def calculate_area(self):
#         return self.__width * self.__height
#
#     def calculate_perimeter(self):
#         return 2 * (self.__width + self.__height)


s = Square(4, 4)
print(s.calculate_area())

t = Triangle(1, 2,3)
print(t.calculate_area())
print(t.calculate_perimeter())