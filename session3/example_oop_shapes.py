import math
import abc

# 1. Define an abstract base class called `Shape` with the following methods:
#   - `area()`: returns the area of the shape
#   - `perimeter()`: returns the perimeter of the shape
#   - `__str__()`: returns a string representation of the shape, in the format "Shape(area=XX, perimeter=YY)"
#   Don't forget to use the @abc.abstractmethod decorator for the first two methods.


class Shape(metaclass=abc.ABCMeta):
    def __init__(self):
        self._area = 0
        self._perimeter = 0

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"Shape(area={self._area}, perimeter={self._perimeter})"

# 2. Define a concrete class called `Rectangle` that inherits from the `Shape` class.
#   The `Rectangle` class should have the following attributes:
#   - `width`: the width of the rectangle
#   - `height`: the height of the rectangle
#   Implement the `area()` and `perimeter()` methods to return the correct values for a rectangle.
#   Also, implement the `__init__()` method to initialize the `width` and `height` attributes.


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 3. Define a concrete class called `Circle` that inherits from the `Shape` class.
#   The `Circle` class should have the following attribute:
#   - `radius`: the radius of the circle
#   Implement the `area()` and `perimeter()` methods to return the correct values for a circle.
#   Also, implement the `__init__()` method to initialize the `radius` attribute.


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 4. Test your implementation by creating a `Rectangle` and a `Circle` object, and printing their area and perimeter.


rectangle = Rectangle(5, 10)
circle = Circle(3)

print(rectangle.area())  # Output: 50
print(rectangle.perimeter())  # Output: 30
print(circle.area())  # Output: 28.274333882308138
print(circle.perimeter())  # Output: 18.84955592153876

# 5. Modify the `__str__()` method in the `Shape` class to include the name of the shape


def __str__(self):
    return f"{self.__class__.__name__}(area={self._area}, perimeter={self._perimeter})"
