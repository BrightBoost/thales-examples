def outer(func):
    def inner(name):
        if name == "m":
          print("ja doei")
        else:
          print("oh hallo")
        func(name)
    return inner

@outer
def hi(name):
  print("oh hi")


hi("c")