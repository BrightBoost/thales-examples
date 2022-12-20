from my_module import calculate_mean, calculate_median
import random


def generate_random_number():
  return random.randint(1, 10)


def generate_random_list(n):
  random_list = []
  for i in range(n):
    random_list.append(generate_random_number())
  return random_list


print(generate_random_number())
print(generate_random_list(5))


random_list = generate_random_list(10)
print(calculate_mean(random_list))
print(calculate_median(random_list))
