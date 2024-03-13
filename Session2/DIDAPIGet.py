import requests
import dotenv
import os

dotenv.load_dotenv()

KEY = os.getenv("DID_KEY")

url = "https://api.d-id.com/clips/clp_h12qfDZv79s7Gx2hRwovz"

headers = {
    "accept": "application/json",
    "authorization": "Basic " + KEY
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())