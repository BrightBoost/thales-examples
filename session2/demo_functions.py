def show_training(topic, level):
    print("This training", topic, "is", level)


def show_students(training, *students):
    print(type(students))
    for student in students:
        print(student, "participates in", training)


show_training("python", "medium")
show_training(level="medium", topic="Python")

show_students("Python", "Dana", "Rik", "Gerald")
show_students("Python", "Dana")
