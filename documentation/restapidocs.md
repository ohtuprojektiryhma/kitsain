# REST API documentation

## POST /generate

Generates a new recipe from given ingredients and conditions.

**Request body:** JSON object with fields:

-   pantry: JSON object, that has the name of the item as the key and amount of the item as the value. These items can be used for the recipe.
-   recipe_type: String of conditions that the recipe must fulfill.

Optional fields in the request body:

-   required_items: JSON object, that has the name of the item as the key and amount of the item as the value, that must be used in the generated recipe. Defaults to `{}`.
-   pantry_only: Boolean that informs whether only pantry items should be used in the generated recipe, defaults to `false`
-   special_supplies: JSON array of special kitchen supplies that can be used in the generated recipe, defaults to `[]`.
-   language: String, the language of the generated recipe.
-   options: Int, how many recipe options are returned

**Returns:** JSON object with fields:

-   recipes: JSON array of JSON objects that each contain fields:
    -   ingredients: JSON object with format "ingredient": "amount".
    -   instructions: JSON array of instruction steps in the order they should be completed.
    -   recipe_name: String, the name of the recipe.

**Example:**

Request

```json
{
    "required_items": {"milk" : "1l"},
    "pantry": {"banana" : "2"},
    "pantry_only": true,
    "recipe_type": "sweet",
    "special_supplies": ["blender"],
    "language": "English",
    "options" : 2
}
```

Response

```json
{
  "recipes": [
    {
      "ingredients": {
        "banana": "2",
        "milk": "1l"
      },
      "instructions": [
        "1. Peel the bananas and cut them into small pieces.",
        "2. In a blender, combine the banana pieces and milk.",
        "3. Blend until smooth and creamy.",
        "4. Pour the banana milkshake into glasses and serve chilled.",
        "5. Enjoy your refreshing Banana Milkshake!"
      ],
      "recipe_name": "Banana Milkshake"
    },
    {
      "ingredients": {
        "banana": "2",
        "milk": "1l"
      },
      "instructions": [
        "1. In a saucepan, heat the milk over medium heat until it starts to simmer.",
        "2. Meanwhile, mash the bananas in a bowl until smooth.",
        "3. Gradually pour the hot milk into the mashed bananas while stirring continuously.",
        "4. Return the mixture to the saucepan and cook until it thickens into a pudding consistency.",
        "5. Remove from heat and let it cool slightly before serving.",
        "6. Garnish with banana slices or a sprinkle of cinnamon if desired.",
        "7. Enjoy your delicious Banana Pudding!"
      ],
      "recipe_name": "Banana Pudding"
    }
  ]
}
```

## POST /change

Changes a given recipe.

**Request body:** JSON object with fields:

-   recipe: JSON object, a recipe in the same format as the output of POST /generate
-   change: String of changes to make to the recipe.

**Returns:** A new recipe in the same format as POST /generate

**Example:**

Request

```json
{
    "recipe": {
        "ingredients": {
            "banana": 2,
            "milk": "2 cups"
        },
        "instructions": [
            "Peel the bananas and slice them into small chunks.",
            "In a blender, add the banana chunks and milk.",
            "Blend until the mixture is smooth and creamy.",
            "Pour the milkshake into glasses and serve immediately."
        ],
        "recipe_name": "Banana Milkshake"
    },
    "change": "add strawberries"
}
```

Response

```json
{
    "ingredients": {
        "banana": 2,
        "milk": "2 cups",
        "strawberries": "1 cup"
    },
    "instructions": [
        "Peel the bananas and slice them into small chunks.",
        "Wash the strawberries and remove the stems.",
        "In a blender, add the banana chunks, strawberries, and milk.",
        "Blend until the mixture is smooth and creamy.",
        "Pour the milkshake into glasses and serve immediately."
    ],
    "recipe_name": "Strawberry Banana Milkshake"
}
```
