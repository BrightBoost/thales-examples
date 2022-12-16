# don't do any of this

x = 7


def print_message(msg):
    print("This is the message outer:", msg)
    x = 3

    def secret_message(msg):
        global x
        print("This is the message inner:", msg, x)
    secret_message("Mijn geheime ww")
    print("x is", x)


print_message("Hoi!")
print(x)
