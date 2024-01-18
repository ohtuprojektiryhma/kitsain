from services.recipe_service import RecipeService

recipe_service = RecipeService()
while True:
    ingredients = input("Input ingredients in pantry:\n")
    print(recipe_service.get_recipe(ingredients, "vegan"))
    stop = input("Type s to stop")
    if stop == "s":
        break
