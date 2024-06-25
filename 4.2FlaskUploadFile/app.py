import os
import bcrypt
from flask import Flask, jsonify, flash, render_template, request, redirect, url_for, session as flask_session
from sqlmodel import Session, select
from pydantic import BaseModel
from ultralytics import YOLO
from database import get_user_by_username, create_user, engine, User
from PIL import Image
import numpy as np
from fer import FER
import cv2
import ast
import re


app = Flask("HermesSight")
app.secret_key = "my_secret_key"
app.config["UPLOAD_FOLDER"] = './uploads'
app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg'}


object_detection_model = YOLO("yolov8n.pt")


# PyDantic models for request validation
class RegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    username: str
    password: str
    check_password: str

class LoginModel(BaseModel):
    username: str
    password: str

def allowed_file(filename):
    extention = filename.split('.')[-1]
    if extention not in app.config["ALLOWED_EXTENSIONS"]:
        return False
    else:
        return True


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about-me")
def about_me():
    return render_template("about-me.html")


@app.route("/about-project")
def about_project():
    return render_template("about-project.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    
    elif request.method == "POST":
        try:
            login_data = LoginModel(
                username=request.form["username"],
                password=request.form["password"]
            )
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("signin"))
        
        user = get_user_by_username(login_data.username)
        if user:
            password_byte = login_data.password.encode("utf-8")
            if bcrypt.checkpw(password_byte, user.password):
                flask_session["user_id"] = user.id  # Using session to store user_id
                return redirect(url_for('profile'))
            else:
                flash("Wrong password", "danger")
                return redirect(url_for("signin"))
        else:
            flash("User not found", "danger")
            return redirect(url_for("signin"))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        try:
            register_data = RegisterModel(
                name=request.form["name"],
                surname=request.form["surname"],
                email=request.form["email"],
                username=request.form["username"],
                password=request.form["password"],
                check_password=request.form["check_password"]
            )
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("register"))
        
        if register_data.password != register_data.check_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for("register"))
        
        if not re.search(r'[A-Z]', register_data.password):
            flash("Uh Uh, no uPpercase in the password :D", "danger")
            return redirect(url_for("register"))
        
        if not re.search(r'\d', register_data.password):
            flash("Uh Uh, no digits in the password 0-o", "danger")
            return redirect(url_for("register"))
        
        if not re.search(r'[@$!%*?&]', register_data.password):
            flash("Uh Uh, no ch@racters in the password :)", "danger")
            return redirect(url_for("register"))
        
        if len(register_data.password) <= 12:
            flash("too short :p", "danger")
            return redirect(url_for("register"))

        with Session(engine) as db_session:
            # Check if the username already exists
            if get_user_by_username(register_data.username):
                flash("No No No, Username already exists", "danger")
                return redirect(url_for("register"))

            # Hash the password
            password_hash = bcrypt.hashpw(register_data.password.encode('utf-8'), bcrypt.gensalt())

            # Create user in the database
            create_user(db_session, register_data.name, register_data.surname, register_data.email, register_data.username, password_hash)

            flash("Sign up successful! Please log in.", "success")
            return redirect(url_for("signin"))


@app.route("/logout")
def logout():
    flask_session.pop("user_id")
    return redirect(url_for("index"))


@app.route("/profile", methods=["GET", "POST"])
def profile():
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    
    emotions_str = request.args.get('emotions')
    objects_str = request.args.get('objects')
    bmr = request.args.get('bmr')

    if emotions_str:
        emotions = ast.literal_eval(emotions_str)
    else:
        emotions = emotions_str

    objects = eval(objects_str) if isinstance(objects_str, str) else objects_str
    
    with Session(engine) as db_session:
        user = db_session.get(User, user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return render_template("profile.html", username=user.username, emotions=emotions, objects=objects, bmr=bmr)


@app.route("/ai-face-analysis", methods=["GET", "POST"])
def ai_face_analysis():
    print("AI started")
    if flask_session.get('user_id'):
        if request.method == "GET":
            return render_template("ai_face_analysis.html")
        elif request.method == "POST":
            print("AI started POST")
            my_image = request.files['image']
            if my_image.filename == "":
                return redirect(url_for('upload'))
            else:
                if my_image and allowed_file(my_image.filename):
                    print(my_image.filename)
                    save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                    my_image.save(save_path)
                    model = FER()
                    frame = cv2.imread(save_path)
                    detected_emotions = model.detect_emotions(frame)

                    emotions = {}

                    for idx, emotion in enumerate(detected_emotions):
                        emotion_list = emotion["emotions"]
                        dominant_emotion = max(emotion_list, key=emotion_list.get)
                        emotions[str(idx)] = dominant_emotion

                    return redirect(url_for('profile', emotions=str(emotions)))
    else:
        return redirect(url_for("index"))


@app.route("/ai-object-detection", methods=["GET", "POST"])
def ai_object_detection():
    if flask_session.get('user_id'):
        if request.method == "GET":
            return render_template("ai_object_detection.html")
        elif request.method == "POST":
            my_image = request.files['image']
            if my_image.filename == "":
                return redirect(url_for('upload'))
            else:
                if my_image and allowed_file(my_image.filename):
                    save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                    my_image.save(save_path)
                    results = object_detection_model(save_path)
                    annotated_img = results[0].plot()
                    annotated_img_path = os.path.join(app.config["UPLOAD_FOLDER"], "annotated_" + my_image.filename)
                    
                    annotated_pil_img = Image.fromarray(np.uint8(annotated_img))
                    annotated_pil_img.save(annotated_img_path)

                    detected_objects = {}
                    names = object_detection_model.names
                    for r in results:
                        for c in r.boxes.cls:
                            if names[int(c)] not in detected_objects:
                                detected_objects[names[int(c)]] = 1
                            else:
                                detected_objects[names[int(c)]] += 1

                    return redirect(url_for('profile', objects=detected_objects))
    else:
        return redirect(url_for("index"))


@app.route("/bmrcalculator", methods=["GET", "POST"])
def bmr_calculator():
    if request.method == "GET":
        return render_template("bmrcalculator.html")
    elif request.method == "POST":
        gender = request.form.get('gender')
        age = int(request.form.get('age'))
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))

        bmr = calculate_bmr(weight, height, age, gender)

        return redirect(url_for('profile', bmr=bmr))
    

def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Must be 'male' or 'female'.")
    return bmr
