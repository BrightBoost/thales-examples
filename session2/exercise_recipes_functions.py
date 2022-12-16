# stap 1
def print_ingredients(**ingredients):
    for i, q in ingredients.items():
        print("Use", q, "of", i)


# stap 2
print_ingredients(pasta="200 gram")
print_ingredients(pasta="200 gram", tomatensaus="2 lepels")


# stap 3
def print_info_recipe(desc, cat="General"):
    print(desc, "falls into category", cat)


# stap 4
print_info_recipe("Havermout")
print_info_recipe("Oatmeal", "breakfast")
print_info_recipe(cat="Dinner", desc="pasta")
