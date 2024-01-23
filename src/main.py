from api_connection import API_Connection
#from services.recipe_service import RecipeService

ingredients = []
api_connection = API_Connection()


while True:
    ingredient = input(
        "Put an ingredient in pantry or generate recipe (g) or stop (s):\n"
    )
    if ingredient == "s":
        break
    if ingredient == "g":
        print(api_connection.request_recipe(ingredients))#, "vegan"))
    else:
        ingredients.append(ingredient)
