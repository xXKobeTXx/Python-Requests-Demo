import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("Success! Here's part of the data:")
    print(response.json())
else:
    print("Request failed:", response.status_code)
