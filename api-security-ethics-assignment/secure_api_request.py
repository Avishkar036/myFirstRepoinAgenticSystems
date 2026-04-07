import os
import requests

api_key = os.getenv("API_KEY")

if not api_key:
    print("API key not found. Please set the API_KEY environment variable.")
    exit()


response = requests.get("https://api.example.com/data", api_key)

if response.status_code == 200:
    print(response.json())

elif response.status_code == 429:
    print("Rate limit reached. Try again later.")

else:
    print("Request failed", response.status_code)