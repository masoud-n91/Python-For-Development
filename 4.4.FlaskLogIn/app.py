import os
from flask import Flask, redirect, request, flash, render_template, url_for, jsonify, session as flask_session
from flask_mail import Mail, Message
from dotenv import load_dotenv
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import database as db
import bcrypt
import re
import google.generativeai as genai
from datetime import datetime

# for AI
from PIL import Image
import numpy as np
from src.face_analysis import FaceAnalysis
from utils.image import encode_image



load_dotenv()

app = Flask("Virtuals")

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.path.dirname(__file__), 'flask_session_cache')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_FILE_THRESHOLD'] = 100


# Email configuration using environment variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ("Virtuals", os.getenv('MAIL_USERNAME'))

mail = Mail(app)
s = URLSafeTimedSerializer(os.getenv('SECRET_KEY', 'SecretKey'))  


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def load_comments():
    
    comments = db.get_comments()
    user_list = []
    comments_list = []

    for comment in comments:
        user_id = comment["user_id"]
        text = comment["comment"]
        print(f"User: {user_id}, Text: {text}")
        print(f"User info: {db.get_guest_by_id(user_id).first_name}, Text: {text}")
        user_list.append(db.get_guest_by_id(user_id).first_name)
        comments_list.append(text)

    combined = list(zip(user_list, comments_list))
    return combined


def google_init():
    genai.api_key = GOOGLE_API_KEY

    generation_config = {
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 4096,
    }

    safety_settings = [
        {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
        },
        {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
        },
        {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
        },
        {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
        },
    ]

    sys_prompt = f"""
    You are a helpful assistant and a GPt
    """

    model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            safety_settings=safety_settings,
            generation_config=generation_config,
            system_instruction=sys_prompt,
        )


    chat_session = model.start_chat()

    return chat_session


chat_session = google_init()



# a function to check the validity of the password
def check_password(password1, password2):
    if password1 != password2:
        flash("Passwords do not match")
        return False

    if not re.search(r'[A-Z]', password1):
        flash("No uppercase in the password")
        return False

    if not re.search(r'\d', password1):
        flash("No digits in the password")
        return False

    if not re.search(r'[@$!%*?&]', password1):
        flash("No characters in the password")
        return False

    if len(password1) <= 12:
        flash("Password is too short")
        return False
    
    return True


# a function to send activation email to Guests
def send_activation_email(email, first_name):
    try:
        token = s.dumps(email, salt='email-confirm')
        print(f"Generated token: {token}")
        msg = Message('Account Activation', 
                      sender=app.config['MAIL_DEFAULT_SENDER'], 
                      recipients=[email])
        
        link = url_for('confirm_guest_email', token=token, _external=True)
        
        msg.body = f'''Hello {first_name},

Please click on the following link to confirm your email address:

{link}

If you did not make this request, please ignore this email.

Best regards,
Virtuals Team
'''
        
        msg.html = f'''
        <h1>Hello {first_name},</h1>
        <p>Please click on the following link to confirm your email address:</p>
        <p><a href="{link}">Activate Your Account</a></p>
        <p>If you did not make this request, please ignore this email.</p>
        <p>Best regards,<br>Virtuals Team</p>
        '''

        mail.send(msg)
        print("Email sent successfully")
        return True
    except Exception as e:
        # Log the error here
        print(f"Error in send_activation_email: {str(e)}")
        return False
    

# a function to send reset password email
def send_reset_password_email(email, first_name, table):
    try:
        token = s.dumps(email, salt='password-reset')
        print(f"Generated token: {token}")
        msg = Message('Reset-Password', 
                      sender=app.config['MAIL_DEFAULT_SENDER'], 
                      recipients=[email])
        
        if table == "admins":
            link = url_for('new_password_admin', token=token, _external=True)
        elif table == "guests":
            link = url_for('new_password_guest', token=token, _external=True)
        else:
            link = url_for('new_password_student', token=token, _external=True)
        
        msg.body = f'''Hello {first_name},

Please click on the following link to reset your password:

{link}

If you did not make this request, please ignore this email.

Best regards,
Virtuals Team
'''
        
        msg.html = f'''
        <h1>Hello {first_name},</h1>
        <p>Please click on the following link to reset your password:</p>
        <p><a href="{link}">Reset Your Password</a></p>
        <p>If you did not make this request, please ignore this email.</p>
        <p>Best regards,<br>Virtuals Team</p>
        '''

        mail.send(msg)
        print("Email sent successfully")
        return True
    except Exception as e:
        # Log the error here
        print(f"Error in send_activation_email: {str(e)}")
        return False


# Homepage
@app.route('/')
def index():
    return render_template("index.html")


# login page for the first VA
@app.route('/virtual1')
def virtual1():
    return render_template("virtual1.html")


# signin page for admin
@app.route('/signin-admin', methods=['GET', 'POST'])
def signin_admin():

    if request.method == 'GET':
        return render_template("signin-admin.html")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        admin_user = db.get_admin_by_email(email)

        if not admin_user:
            flash('Invalid email or password. Please try again.')
            return render_template("signin-admin.html")
        
        if not admin_user.is_active:
            flash('Your account is not activated. Please activate your account.')
            return render_template("signin-admin.html")

        if not bcrypt.checkpw(password.encode('utf-8'), admin_user.password.encode('utf-8')):
            flash('Invalid email or password. Please try again.')
            return render_template("signin-admin.html")

        flask_session["user_id"] = ["admins", email, admin_user.first_name + " " + admin_user.family_name]
        return redirect(url_for('admin_dashboard'))


# this signup page is just the same as signin page but the slider is overlapping with signin
@app.route('/signup-admin', methods=['GET','POST'])
def signup_admin():

    if request.method == 'GET':
        return render_template("signup-admin.html")

    if request.method == 'POST':
        first_name = request.form['first_name']
        family_name = request.form['family_name']
        email = request.form['email']
        password1 = request.form['password']
        password2 = request.form['repassword']

        admin_user = db.get_admin_by_email(email)
        if admin_user:
            if admin_user.is_active:
                flash('Email already exists. Please login if your account is approved by Prof. Nait-ali.')
                return redirect(url_for("signup_admin"))
            else:
                db.delete_user(database="admins", email=email)

        if not check_password(password1, password2):
            return redirect(url_for("signup_admin"))

        hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        join_time = datetime.now()

        db.create_user(database="admins", first_name=first_name, family_name=family_name, email=email, password=hashed_password, join_time=join_time)

        flash('Account created successfully. Please contact Prof. Nait-ali to activate your account.')

        return redirect(url_for('signin_admin'))


# signin page for student
@app.route('/signin-student', methods=['GET', 'POST'])
def signin_student():
    if request.method == 'GET':
        return render_template("signin-student.html")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        student_user = db.get_student_by_email(email)
        
        if not student_user:
            flash('Invalid email or password. Please try again.')
            return render_template("signin-student.html")
        
        if not student_user.is_active:
            flash('Your account is not activated. Please contact administration to activate your account.')
            return render_template("signin-student.html")

        if not bcrypt.checkpw(password.encode('utf-8'), student_user.password.encode('utf-8')):
            flash('Invalid email or password. Please try again.')
            return render_template("signin-student.html")

        flask_session["user_id"] = ["students", email, student_user.first_name + " " + student_user.family_name]
        return redirect(url_for('chatbot_student'))


# this signup page is just the same as signin page but the slider is overlapping with signin
@app.route('/signup-student', methods=['GET', 'POST'])
def signup_student():
    
    print("signup-student")
    if request.method == 'GET':
        print("signup-student GET")
        return render_template("signup-student.html")
    
    if request.method == 'POST':
        print("signup-student POST")
        first_name = request.form['first_name']
        family_name = request.form['family_name']
        student_number = request.form['student_number']
        email = request.form['email']
        password1 = request.form['password']
        password2 = request.form['repassword']

        student_user = db.get_student_by_email(email)
        if student_user:
            if student_user.is_active:
                flash('Email already exists. Please login if your account is approved by administration.')
                return redirect(url_for("signup_student"))
            else:
                db.delete_user(database="students", email=email)

        if not check_password(password1, password2):
            return redirect(url_for("signup_student"))

        hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        join_time = datetime.now()

        db.create_user(database="students", first_name=first_name, family_name=family_name, email=email, password=hashed_password, join_time=join_time, student_number=student_number)

        flash('Account created successfully. Please contact the administration to activate your account.')

        return redirect(url_for('signin_student'))


#  signin page for guest
@app.route('/signin-guest', methods=['GET', 'POST'])
def signin_guest():

    if request.method == 'GET':
        return render_template("signin-guest.html")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        guest_user = db.get_guest_by_email(email)

        print("guest_user: ", guest_user)
        
        if not guest_user:
            flash('Invalid email or password. Please try again.')
            return render_template("signin-guest.html")
        
        if not guest_user.is_active:
            flash('Your account is not activated. Please activate your account in signup page.')
            return render_template("signin-guest.html")

        if not bcrypt.checkpw(password.encode('utf-8'), guest_user.password.encode('utf-8')):
            flash('Invalid email or password. Please try again.')
            return render_template("signin-guest.html")

        flask_session["user_id"] = ["guests", email, guest_user.first_name + " " + guest_user.family_name]
        return redirect(url_for('webapp_guest'))


# this signup page is just the same as signin page but the slider is overlapping with signin
@app.route('/signup-guest', methods=['GET', 'POST'])
def signup_guest():

    if request.method == 'GET':
        return render_template("signup-guest.html")

    if request.method == 'POST':
        first_name = request.form['first_name']
        family_name = request.form['family_name']
        email = request.form['email']
        password1 = request.form['password']
        password2 = request.form['repassword']

        guest_user = db.get_guest_by_email(email)
        if guest_user:
            if guest_user.is_active:
                flash('Email already exists. Please login.')
                return redirect(url_for("signup_guest"))
            else:
                db.delete_user(database="guests", email=email)
        
        if not check_password(password1, password2):
            return redirect(url_for("signup_guest"))

        hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        join_time = datetime.now()

        db.create_user(database="guests", first_name=first_name, family_name=family_name, email=email, password=hashed_password, join_time=join_time)

        result = send_activation_email(email, first_name)

        if result:
            flash('Account created successfully. An email is sent to you. Use the link to activate your account.')
            return redirect(url_for('signin_guest'))
        
        else:
            db.delete_user(database="guests", email=email)
            flash('Something went wrong. Please try again. Enter a valid email.')
            return redirect(url_for('signin_guest'))
        

# when guests click on the link in the email for activation, they get redirected to this page
@app.route('/confirm_guest_email/<token>')
def confirm_guest_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        print(f"Decoded email: {email}")
    except (SignatureExpired, BadSignature):
        return render_template('confirm_email.html', message="The confirmation link is invalid or has expired.")
    
    try:
        db.activate_guest(email)
        return render_template('confirm_email.html', message="Thank you for confirming your email address.")
    except Exception as e:
        return render_template('confirm_email.html', message="An error occurred while confirming your email. Please try again later.")


#  a page to get email address and send reset password email for guests
@app.route('/forget-password-guest', methods=['GET', 'POST'])
def forget_password_guest():

    if request.method == 'GET':
        return render_template('forget-password-guest.html')

    if request.method == 'POST':
        email = request.form['forgotten_email']
        print(f"Email: {email}")
        user = db.get_guest_by_email(email)
        print(f"User: {user}")

        if user and user.is_active:
            result = send_reset_password_email(email, user.first_name, "guests")
            if result:
                flash('An email has been sent to your inbox. Please click on the link to reset your password.')
            else:
                flash('An error occurred while sending the email. Please try again later.')
            return redirect(url_for("forget_password_guest"))
            
        else:
            flash('Invalid email. Please make sure that you have an active account.')
            return redirect(url_for("forget_password_guest"))


#  when guest clickes on the reset password link in the email, they get redirected to this page
@app.route('/new-password-guest/<token>')
def new_password_guest(token):

    try:
        email = s.loads(token, salt='password-reset', max_age=3600)
        print(f"Decoded email: {email}")
    except (SignatureExpired, BadSignature):
        return render_template('new-password-guest.html', email=email, message="The confirmation link is invalid or has expired.")
    
    try:
        return render_template('new-password-guest.html', email=email, message="Thank you for confirming your email address. Now please enter your new password.")
    except Exception as e:
        return render_template('new-password-guest.html', email=email, message="An error occurred while confirming your email. Please try again later.")


#  when guest enters new password, they get redirected to this page
@app.route('/update-password-guest', methods=['GET', 'POST'])
def update_password_guest():

    email = request.form['email']
    print(f"Email: {email}")
    password1 = request.form['password']
    password2 = request.form['repassword']

    if not check_password(password1, password2):
        return render_template('update-password-guest.html')

    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())

    db.update_password("guests", email, hashed_password)

    flash("Your password has been changed successfully. Please login with your new password.")

    return redirect(url_for('signin_guest'))


#  a page to get email address and send reset password email for students
@app.route('/forget-password-student', methods=['GET', 'POST'])
def forget_password_student():

    if request.method == 'GET':
        return render_template('forget-password-student.html')

    if request.method == 'POST':
        email = request.form['forgotten_email']
        print(f"Email: {email}")
        user = db.get_student_by_email(email)
        print(f"User: {user}")

        if user and user.is_active:
            result = send_reset_password_email(email, user.first_name, "students")
            if result:
                flash('An email has been sent to your inbox. Please click on the link to reset your password.')
            else:
                flash('An error occurred while sending the email. Please try again later.')
            return redirect(url_for("forget_password_student"))
            
        else:
            flash('Invalid email. Please make sure that you have an active account.')
            return redirect(url_for("forget_password_student"))


#  when student clickes on the reset password link in the email, they get redirected to this page
@app.route('/new-password-student/<token>')
def new_password_student(token):

    try:
        email = s.loads(token, salt='password-reset', max_age=3600)
        print(f"Decoded email: {email}")
    except (SignatureExpired, BadSignature):
        return render_template('new-password-student.html', email=email, message="The confirmation link is invalid or has expired.")
    
    try:
        return render_template('new-password-student.html', email=email, message="Thank you for confirming your email address. Now please enter your new password.")
    except Exception as e:
        return render_template('new-password-student.html', email=email, message="An error occurred while confirming your email. Please try again later.")


#  when student enters new password, they get redirected to this page
@app.route('/update-password-student', methods=['GET', 'POST'])
def update_password_student():

    email = request.form['email']
    print(f"Email: {email}")
    password1 = request.form['password']
    password2 = request.form['repassword']

    if not check_password(password1, password2):
        return render_template('update-password-student.html')

    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())

    db.update_password("students", email, hashed_password)

    flash("Your password has been changed successfully. Please login with your new password.")

    return redirect(url_for('signin_student'))


#  a page to get email address and send reset password email for admins
@app.route('/forget-password-admin', methods=['GET', 'POST'])
def forget_password_admin():

    if request.method == 'GET':
        return render_template('forget-password-admin.html')

    if request.method == 'POST':
        email = request.form['forgotten_email']
        print(f"Email: {email}")
        user = db.get_admin_by_email(email)
        print(f"User: {user}")

        if user and user.is_active:
            result = send_reset_password_email(email, user.first_name, "admins")
            if result:
                flash('An email has been sent to your inbox. Please click on the link to reset your password.')
            else:
                flash('An error occurred while sending the email. Please try again later.')
            return redirect(url_for("forget_password_admin"))
            
        else:
            flash('Invalid email. Please make sure that you have an active account.')
            return redirect(url_for("forget_password_admin"))


#  when admin clickes on the reset password link in the email, they get redirected to this page
@app.route('/new-password-admin/<token>')
def new_password_admin(token):

    try:
        email = s.loads(token, salt='password-reset', max_age=3600)
        print(f"Decoded email: {email}")
    except (SignatureExpired, BadSignature):
        return render_template('new-password-admin.html', email=email, message="The confirmation link is invalid or has expired.")
    
    try:
        return render_template('new-password-admin.html', email=email, message="Thank you for confirming your email address. Now please enter your new password.")
    except Exception as e:
        return render_template('new-password-admin.html', email=email, message="An error occurred while confirming your email. Please try again later.")


#  when admin enters new password, they get redirected to this page
@app.route('/update-password-admin', methods=['GET', 'POST'])
def update_password_admin():

    email = request.form['email']
    print(f"Email: {email}")
    password1 = request.form['password']
    password2 = request.form['repassword']

    if not check_password(password1, password2):
        return render_template('update-password-admin.html')

    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())

    db.update_password("admins", email, hashed_password)

    flash("Your password has been changed successfully. Please login with your new password.")

    return redirect(url_for('signin_admin'))


def time_since(dt):
    now = datetime.now()
    delta = now - dt
    
    seconds = delta.total_seconds()
    
    if seconds < 60:
        return f"{int(seconds)} seconds before"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{int(minutes)} minutes before"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{int(hours)} hours before"
    elif seconds < 604800:  # 7 days
        days = seconds // 86400
        return f"{int(days)} days before"
    elif seconds < 31536000:  # 365 days
        weeks = seconds // 604800
        return f"{int(weeks)} weeks before"
    else:
        years = seconds // 31536000
        return f"{int(years)} years before"


@app.route('/admin-dash')
def admin_dashboard():

    admins = db.read_admins()  

    names = []

    for admin in admins:
        name = admin[1] + " " + admin[2]
        email = admin[3]
        raw_date = admin[6]
        date = time_since(raw_date)

        names.append([name, email, date, "11.jpg"])
    
    return render_template('admin-dash.html', names=names, enumerate=enumerate)


@app.route('/dashboard-activations')
def dashboard_activations():
    tables = ["students"]
    return render_template('dashboard-activations.html', tables=tables, enumerate=enumerate)


@app.route('/get_table_auth', methods=['POST'])
def get_table_auth():
    table_name = request.json.get('table_name')
    data = db.fetch_table_auth(table_name)
    return jsonify(data)


# show contents of table
@app.route('/get_table_data', methods=['POST'])
def get_table_data():
    table_name = request.json.get('table_name')
    data = db.fetch_table_data(table_name)
    return jsonify(data)


# show all table names
@app.route('/show-tables')
def show_tables():
    tables = db.get_tables()
    return render_template('show-tables.html', tables=tables)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    flask_session.pop("user_id")
    return redirect(url_for("index"))


@app.route('/gen-response', methods=['POST'])
def generate_response():
    
    try:
        data = request.get_json()

        user_text = data['prompt']

        response = chat_session.send_message(user_text)
        response_text = response.text

        response_data = {
            'choices': [
                {'text': response_text}
            ]
        }

        return jsonify(response_data), 200

    except Exception as e:
        error_message = "Error processing request: " + str(e)
        print(error_message)
        return jsonify({'error': error_message}), 500
    

@app.route("/about-me")
def about_me():
    return render_template("about-me.html")


@app.route("/about-project")
def about_project():
    return render_template("about-project.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/webapp-guest")
def webapp_guest():
    user_id = flask_session.get("user_id")
    print(f"session: {flask_session}")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))
    
    return render_template("webapp-guest.html", username=user_id[2])


# these enpoints must connect to the chatbot app
@app.route('/chatbot-guest')
def chatbot_guest():
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))
    return render_template('chatbot-guest.html')


@app.route('/chatbot-student')
def chatbot_student():
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))
    return render_template('chatbot-student.html')


@app.route('/chatbot-admin')
def chatbot_admin():
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))
    return render_template('chatbot-admin.html')


# ai endpoints:

app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg'}

face_analysis = FaceAnalysis("models/det_10g.onnx", "models/genderage.onnx")


def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route("/ai-face-analysis", methods=["GET", "POST"])
def ai_face_analysis():
    user_id = flask_session.get("user_id")
    comments = db.get_comments()
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))

    if request.method == 'POST':
        image = request.files['image']
        if image.filename == "":
            flash("No selected file", "warning")
            return redirect(url_for("ai_face_analysis"))

        if image and allowed_files(image.filename):
            try:
                input_image = Image.open(image.stream)
                input_image = np.array(input_image)
                output_image, genders, ages = face_analysis.detect_age_gender(input_image)
                image_uri = encode_image(output_image)

                return render_template("ai-face-analysis.html", genders=genders, ages=ages, image_uri=image_uri, username=user_id[2], comments=comments)
            except Exception as e:
                flash(f"Error processing image: {e}", "danger")
                return redirect(url_for("ai_face_analysis"))
        flash("File type not allowed", "warning")
        return redirect(url_for("ai_face_analysis"))
    
    return render_template("ai-face-analysis.html", username=user_id[2], comments=comments)


def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr


@app.route("/bmr", methods=["GET", "POST"])
def bmr():
    print("BMR CALLED")
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))
    
    print(f"user_id: {user_id}")

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        age = int(request.form["age"])
        gender = request.form["gender"]
        bmr_result = calculate_bmr(weight, height, age, gender)
        return render_template("bmr.html", bmr_result=bmr_result, username=user_id[2])
    
    return render_template("bmr.html", bmr_result=None, username=user_id[2])


@app.route("/mind-reader", methods=["GET", "POST"])
def mind_reader():
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))

    if request.method == "POST":
        x = request.form["number"]
        if not x:
            flash("Please enter a number", "warning")
            return redirect(url_for("mind_reader"))
            
        flask_session['number'] = x
        print(x)
        return redirect(url_for('mind_reader_result', number=x))

    return render_template("mind-reader.html", username=user_id[2])


@app.route("/mind-reader-result")
def mind_reader_result():
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))
    # if 'number' not in flask_session:
    #     flash("First enter a number", "warning")
    #     return redirect(url_for("mind_reader"))
    y = request.args.get("number")
    flask_session.pop('number', None)
    return render_template("mind-reader-result.html", number=y, username=user_id[2])


@app.route("/pose-detection")
def pose_detection():
    user_id = flask_session.get("user_id")
    if not user_id:
        flash("Please log-in", "warning")
        return redirect(url_for('virtual1'))

    return render_template("pose-detection.html")


@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    comment = request.form["commentText"]
    username = request.form["username"]
    user = flask_session.get("user_id")

    if user[0] == "guests":
        user_id = db.get_guest_by_email(user[1]).id
        db.submit_comment(user_id, comment)
    if user[0] == "students":
        print(f"Student: {user}")
    if user[0] == "admins":
        print(f"Admin: {user}")

    comments = load_comments()
    print(f"Comments: {comments}")

    return render_template("ai-face-analysis.html", username=user[2], comments=comments)