# create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# use list comprehension to create a new list of square numbers
squares = [x**2 for x in numbers]

# print the new list of square numbers
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

odd_squares = [x**2 for x in numbers if x % 2 != 0]
print(odd_squares)


