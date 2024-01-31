class Pantry:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def display_contents(self):
        print("Pantry contents:")
        for ingredient in self.ingredients:
            print(ingredient)


class Ingredient:
    def __init__(self, name, amount, barcode):
        self.name = name
        self.amount = amount
        self.barcode = barcode

    def __str__(self):
        return f"{self.name}, {self.amount}: {self.barcode}"
