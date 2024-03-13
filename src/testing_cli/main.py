from api_connection import APIConnection

ingredients = []
api_connection = APIConnection()


while True:
    ingredient = input(
        "Put an ingredient in pantry or generate recipe (g) or stop (s):\n"
    )
    if ingredient == "s":
        break
    if ingredient == "g":
        print(api_connection.request_recipe(ingredients, "finnish"))  # , "vegan"))
    else:
        ingredients.append(ingredient)
