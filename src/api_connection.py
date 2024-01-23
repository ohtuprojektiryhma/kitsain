import requests


class API_Connection:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
        self.auth_credentials = ("kitsain", "kitsain")

    def request_recipe(self, ingredients: list):
        data = {"recipe_type": "vegan", "ingredients": ingredients}
        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post(
            f"{self.base_url}/generate/?format=json",
            json=data,
            headers=headers,
            #auth=self.auth_credentials,
        )

        if response.status_code == 201:
            print("Recipe created successfully!")
            print(response.json())  # Print the response data
        else:
            print(f"Error: {response.status_code}")
            print(response.json())  # Print the error details


# response = requests.post(
#    f'{baseUrl}/generate/?format=json', json=data, headers=headers
# )
