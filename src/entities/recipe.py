class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.format_ingredients()
        self.format_instructions()

    def __str__(self) -> str:
        return f"{self.name}\n\n {self.ingredients} \n\n {self.instructions}"

    def format_ingredients(self):
        ingredient_list = ""
        for ingredient in self.ingredients:
            ingredient_list += f"{ingredient} : {self.ingredients[ingredient]}\n"
        self.ingredients = ingredient_list

    def format_instructions(self):
        instruction_list = ""
        for step in self.instructions:
            instruction_list += f"{step}\n"
        self.instructions = instruction_list
