class User:
    def __init__(self, username):
        self.username = username


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi! I'm " + self.name)


class Employee(Person, User):
    def __init__(self, name, age, job, username):
        super().__init__(name, age)
        super(Person, self).__init__(username)

        # alternatively, slight differences (dependency injection)
        # Person.__init__(self, name, age)
        # User.__init__(self, username)
        self.job = job

    def say_hi(self):
        print("Hi! I'm", self.name, "and I'm a",
              self.job, ". My username is", self.username)


e = Employee("maaike", 31, "trainer", "m123")
e.say_hi()
