from fastapi import FastAPI, UploadFile, Form, HTTPException
import face_recognition
import sqlite3
import numpy as np
import cv2

app = FastAPI()


@app.post("/")
def read_root():
    return {"Identify yourself": "Give me your name and an image of your face, and I will identify you."}

@app.post("/identify")
async def identify(username: str = Form(None), password: str = Form(None), image: UploadFile = Form(...)):
    if username == None or password == None:
        raise HTTPException(status_code=400, detail="Username or password cannot be empty")
    if image == None:
        raise HTTPException(status_code=400, detail="Image cannot be empty")
    
    # read database
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IDs")
    rows = cursor.fetchall()
    ids = {}
    for row in rows:
        ids[row[1]] = row[2]

    # check if username and password are valid
    if username not in ids or ids[username] != password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    # read image from the available images
    img = cv2.imread(f"Faces/{username}.jpg")
    orginal_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # read image from the uploaded image
    contents = await image.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    input_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # compare faces
    orginal_face_encoding = face_recognition.face_encodings(orginal_image)[0]
    input_face_encoding = face_recognition.face_encodings(input_image)[0]

    results = face_recognition.compare_faces([orginal_face_encoding], input_face_encoding)

    # return result
    if results[0] == True:
        return {"Identified": "Your face has been identified successfully"}
    else:
        return {"Identified": "Your face has not been identified"}
