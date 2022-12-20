import abc


class Animal(metaclass=abc.ABCMeta):
    """Abstract base class for animals."""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    """Concrete class for dogs."""

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    """Concrete class for cats."""

    def make_sound(self):
        return "Meow!"


dog1 = Dog("Buddy")
print(dog1.name)  # Output: "Buddy"
print(dog1.make_sound())  # Output: "Woof!"

cat1 = Cat("Fluffy")
print(cat1.name)  # Output: "Fluffy"
print(cat1.make_sound())  # Output: "Meow!"

