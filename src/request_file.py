import requests

baseUrl = "http://127.0.0.1:8000"

data = {
    "name": "test",
    "ingredients": [{"ingredient": "cheese"}, {"ingredient": "meat"}],
    "steps": [{"step": "1. cheese on meat"}],
}

auth_credentials = ("kitsain", "kitsain")

#data = {
#    'recipe_type': 'vegan',
#    'ingredients': ['butter', 'milk',
#                    'french-fries', 'tofu',
#                    'beans', 'noodles', 'rice',
#                    'coconut milk', 'curry paste']
#}

headers = {
    "Content-Type": "application/json",
}


response = requests.post(
    f"{baseUrl}/recipes/?format=json", json=data, headers=headers, auth=auth_credentials
)

#response = requests.post(
#    f'{baseUrl}/generate/?format=json', json=data, headers=headers
#)

if response.status_code == 201:
    print("Recipe created successfully!")
    print(response.json())  # Print the response data
else:
    print(f"Error: {response.status_code}")
    print(response.json())  # Print the error details
