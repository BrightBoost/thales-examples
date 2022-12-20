# Define a function that takes a list of dictionaries and a key function
def sort_people(people, key_func):
    # Use the sorted function to sort the list of dictionaries by the key function
    sorted_people = sorted(people, key=key_func)
    return sorted_people


# Define a lambda function that takes a dictionary and returns the age
def get_age(person): return person['age']

# Define a lambda function that takes a dictionary and returns the name


def get_name(person): return person['name']

# Define a lambda function that takes two dictionaries and returns the difference in age


def compare_ages(a, b): return a['age'] - b['age']


# Define a list of dictionaries representing people
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20},
]

# Sort the list of dictionaries by age using the sort_people function and the get_age lambda function
sorted_by_age = sort_people(people, get_age)
# prints: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print(sorted_by_age)

# Sort the list of dictionaries by name using the sort_people function and the get_name lambda function
sorted_by_name = sort_people(people, get_name)
# prints: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
print(sorted_by_name)

# Sort the list of dictionaries by the difference in age using the sort_people function and the compare_ages lambda function
sorted_by_age_difference = sort_people(people, compare_ages)
# prints: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print(sorted_by_age_difference)
