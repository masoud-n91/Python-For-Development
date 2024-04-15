import requests
import dotenv
import os

def main(filename):

    dotenv.load_dotenv()

    KEY = os.getenv("PLANET_KEY")

    url = "https://my-api.plantnet.org/v2/identify/all"

    payload = {
        "api-key": KEY,
    }

    headers = {
    }

    files = {
        "images": open(filename, "rb"),
    }

    response = requests.post(url, params=payload, headers=headers, files=files)

    print("===================")
    print(response.status_code)
    print(response.json())
    print("===================")

    try:
        flower_name = response.json()["results"][0]["species"]["family"]["scientificName"]
    except:
        flower_name = "Unknown"

    return flower_name

if __name__ == "__main__":
    filename = "Session2/Media/plant1.jpeg"
    result = main(filename)
    print(result)