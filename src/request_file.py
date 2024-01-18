import requests

baseUrl = "http://127.0.0.1:8000"

data = {
    "name": "test",
    "ingredients": [{"name": "cheese"}, {"name": "meat"}],
    "steps": [{"description": "cheese on meat"}],
}

auth_credentials = ("kitsain", "kitsain")

headers = {
    "Content-Type": "application/json",
}


response = requests.post(
    f"{baseUrl}/recipes/?format=api", json=data, headers=headers, auth=auth_credentials
)

if response.status_code == 201:
    print("Recipe created successfully!")
    print(response.json())  # Print the response data
else:
    print(f"Error: {response.status_code}")
    print(response.json())  # Print the error details
