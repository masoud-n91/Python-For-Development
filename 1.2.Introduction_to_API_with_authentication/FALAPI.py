import requests
import dotenv
import os

def main(prompt):

    dotenv.load_dotenv()

    KEY = os.getenv("FAL_KEY")

    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"

    headers = {
        "Authorization": "Key " + KEY,
        "Content-type": "application/json"
    }

    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png",
        "prompt": f"(masterpiece:1.4), (best quality), (detailed), {prompt}",
        # "negative_prompt": "(worst quality, poor detailes:1.4), (low quality)",
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response.status_code)
    # print(response.json())

    return response.json()["image"]["url"]


if __name__ == "__main__":
    url = main("a Geraniums in a veil")
    print(url)