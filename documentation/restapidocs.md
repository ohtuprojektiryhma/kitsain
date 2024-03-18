# REST API documentation

## POST /generate

Generates a new recipe from given ingredients and conditions.

**Request body:** JSON object with fields:

-   pantry: JSON array of ingredients as strings. These ingredients can be used for the recipe.
-   recipe_type: String of conditions that the recipe must fulfill.

Optional fields in the request body:

-   required_items: JSON array of ingredients that must be used in the generated recipe. Defaults to `[]`.
-   pantry_only: Boolean that informs whether only pantry items should be used in the generated recipe, defaults to `false`
-   special_supplies: JSON array of special kitchen supplies that can be used in the generated recipe, defaults to `[]`.
-   language: String, the language of the generated recipe.

**Returns:** JSON object with fields:

-   ingredients: JSON object with format "ingredient": "amount".
-   instructions: JSON array of instruction steps in the order they should be completed.
-   recipe_name: String, the name of the recipe.

**Example:**

Request

```json
{
    "required_items": ["milk"],
    "pantry": ["banana"],
    "pantry_only": true,
    "recipe_type": "sweet",
    "special_supplies": ["blender"],
    "language": "English"
}
```

Response

```json
{
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
