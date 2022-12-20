# 1. Create three classes: shape, square, circle
# 2. One should be the base class, choose the logical One
# 3. One should be abstract, choose a logical One
# 3. a Give a specific attribute to the non-abstract classes
# 4. All classes should have an attribute surface and a method calc circumference
# 5. calc circumference should be abstract in Shape
import abc
import math


class Shape(abc.ABC):
    def __init__(self, surface) -> None:
        super().__init__()
        self.surface = surface

    @abc.abstractmethod
    def calc_circumference(self):
        pass

    @abc.abstractmethod
    def calc_surface(self):
        pass


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side
        super().__init__(self.calc_surface())

    def calc_surface(self):
        return self.side ** 2

    def calc_circumference(self):
        return 4 * self.side


class Circle(Shape):
    def __init__(self, r) -> None:
        self.r = r
        super().__init__(self.calc_surface())

    def calc_surface(self):
        return 0.5 * math.pi * self.r ** 2

    def calc_circumference(self):
        return 2 * math.pi * self.r


c = Circle(2)
print(c.calc_circumference())

s = Square(3)
print(s.calc_circumference())