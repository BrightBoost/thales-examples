# In this demo
# create a class dish with a name, country of origin, list of ingredients, and a description of the recipe
# instantiate the instructor's favorite dish

class Dish:
    # constructor
    def __init__(self, name, country, ingredients, description):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.description = description

    # method
    def print_recipe(self):
        print(f"These are the ingredients: {self.ingredients}")
        print(f"Here's the description: {self.description}")

# in fav_dish zit de object referentie
fav_dish = Dish("linzensoep", "geen idee",
                "linzen, tomaat, gember, enzo", "doe het in een pan")
fav_dish.print_recipe()