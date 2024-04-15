import requests
import dotenv
import os

dotenv.load_dotenv()

KEY = os.getenv("ICONFINDER_KEY")

url = "https://api.iconfinder.com/v4/icons/search?query=arrow&count=10"

headers = {
    "Authorization": 'Bearer ' + KEY,
    "accept": "application/json"
    }
response = requests.get(url, headers=headers)

print(f"status_code: {response.status_code}")
print(f"response: {response.json()}")