import requests


class APIConnection:
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000"

    def request_recipe(self, ingredients: list, language: str = "english"):
        data = {
            "recipe_type": "vegan",
            "ingredients": ingredients,
            "language": language,
        }
        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post(
            f"{self.base_url}/generate",
            json=data,
            headers=headers,
        )

        if response.status_code == 200:
            print("Recipe created successfully!")
            print(response.json())  # Print the response data
        else:
            print(f"Error: {response.status_code}")
            print(response.json())  # Print the error details


# response = requests.post(
#    f'{baseUrl}/generate/?format=json', json=data, headers=headers
# )
