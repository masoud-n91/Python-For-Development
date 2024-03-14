import sys
import FALAPI
import PlanetAPI
import requests
import cv2

def main():
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        print("Input flower name:", input_string)
    else:
        print("Please provide a string as input.")

    prompt = f"put {input_string} in a vase in the center of the image with a solid white background"
    url = FALAPI.main(prompt)
    
    response = requests.get(url)

    filename = "Session2/Media/flower.png"
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully as:", filename)
    else:
        print("Failed to download image. Status code:", response.status_code)

    img = cv2.imread(filename)
    cv2.imshow("generated flower", img)
    cv2.waitKey(0)

    flower_name = PlanetAPI.main(filename)
    print(f"Output flower name: {flower_name}")


if __name__ == "__main__":
    main()
