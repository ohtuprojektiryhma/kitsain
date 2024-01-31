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


ingredient1 = Ingredient("ground beef", "400 g", "6407840041172")
ingredient2 = Ingredient("macaroni", "400 g", "6417700050725")

pantry = Pantry()
pantry.add_ingredient(ingredient1)
pantry.add_ingredient(ingredient2)
print(pantry.display_contents())
