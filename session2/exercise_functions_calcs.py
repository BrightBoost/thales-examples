import math


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nearest_prime(n):
    up = n + 1
    down = n - 1

    if is_prime(n):
        return n
    # find nearest up
    while not is_prime(up):
        up = up + 1

    # find nearest down
    while not is_prime(down):
        down = down - 1

    if (n - down) > (up - n):
        return up
    else:
        return down


print(nearest_prime(11))
print(nearest_prime(27))
print(nearest_prime(29))
