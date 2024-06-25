from fer import FER
import cv2
import json
import numpy as np

# Initialize the FER model
model = FER()

# Load an image using OpenCV
image_path = 'uploads/2.jpg'  # Replace with your image file path
frame = cv2.imread(image_path)

# Detect emotions in the image
detected = model.detect_emotions(frame)

# Function to convert ndarray to list recursively
def convert_to_json(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {key: convert_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json(item) for item in obj]
    else:
        return obj  # Handle other types if needed

# Convert ndarray and other non-serializable types to JSON serializable types
detected_serializable = convert_to_json(detected)

# Serialize the detected results to JSON
json_str = json.dumps(detected_serializable)

# Deserialize JSON back into Python data structures (list of dictionaries)
list_of_dicts = json.loads(json_str)

# Print the resulting list of dictionaries
print(list_of_dicts)
print("type: ", type(list_of_dicts))
print("type: ", type(list_of_dicts[0]))

print(len(list_of_dicts))


eee = {}

for i, e in enumerate(list_of_dicts):
    emotion = e["emotions"]
    dominant_emotion = max(emotion, key=emotion.get)
    eee[str(i)] = dominant_emotion

print("eee: ", eee)

print(len(eee))


