import requests
import dotenv
import os

dotenv.load_dotenv()

KEY = os.getenv("DID_KEY")

url = "https://api.d-id.com/clips"

payload = {
    "script": {
        "type": "text",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false",
        "input": "Hi there, I am your virtual assistant. How can I help you?"
    },
    "config": { "result_format": "mp4" },
    "presenter_config": { "crop": { "type": "wide" } },
    "background": { "color": "false" },
    "presenter_id": "anita-6_uTzyZtNR"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic " + KEY
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())