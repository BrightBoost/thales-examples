# We are going to sort a list of dictonaries in multiple ways
# We’ll use lambdas that we pass in as arguments to our sort function to achieve this

alice = {"name": "Alice", "age": 25}
bob = {"name": "Bob", "age": 35}
charle = {"name": "Charle", "age": 20}

people = [alice, bob, charle]


def sort_people(people, key_func):
    return sorted(people, key=key_func)


compare_age = lambda p1, p2: p1["age"] - p2["age"]
get_age = lambda p: p["age"]
get_name = lambda p: p["name"]

sort_by_age = sort_people(people, get_age)
sort_by_name = sort_people(people, get_name)

print(sort_by_age)
print(sort_by_name)
