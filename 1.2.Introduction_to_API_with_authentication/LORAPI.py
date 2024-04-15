import requests
import dotenv
import os

dotenv.load_dotenv()

KEY = os.getenv("LOR_KEY")


headers = {"Authorization": "Bearer " + KEY}
response = requests.get("https://the-one-api.dev/v2/quote", headers=headers)

print(f"status_code: {response.status_code}")
print(f"response: {response.json()}")