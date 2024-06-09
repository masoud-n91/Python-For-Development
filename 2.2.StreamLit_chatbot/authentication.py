import streamlit as st
from sqlmodel import Session, select
from models import User
from streamlit_option_menu import option_menu
import re


class StreamlitAuth:
    def __init__(self, engine):
        self.engine = engine
        self.user = st.session_state.get("user", None)

    
    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    

    def is_valid_password(self, password):
        if (
            re.search(r"[A-Z]", password) is None or
            re.search(r"\d", password) is None or
            re.search(r"[^A-Za-z0-9]", password) is None
        ):
            return False
        return True

    def signup(self):
        st.title("Sign Up")
        name = st.text_input("Name", placeholder="John Doe")
        email = st.text_input("Email", placeholder="JohnDoe@example.com")
        username = st.text_input("Username", placeholder="Johnny")
        password = st.text_input("Password", placeholder="A very hard passw0rd!", type="password")
        st.write("* Password must:\n\t* be atleast 8 characters long\n\t* contain at least one capital letter\n\t* contain at least one number\n\t* contain at least one special character")

        if st.button("Sign Up"):
            if not self.is_valid_email(email):
                st.error("Invalid email format")
            elif len(password) < 8:
                st.error("Your password must be at least 8 characters long")
            elif not self.is_valid_password(password):
                st.error("Your password must contain a capital letter, a number, and a special character")
            else:
                with Session(self.engine) as session:
                    existing_user = session.exec(select(User).where(User.username == username)).first()
                    if existing_user:
                        st.error("Username already exists")
                    else:
                        user = User(name=name, email=email, username=username, password=password)
                        session.add(user)
                        session.commit()
                        st.success("You have successfully signed up!")

    def signin(self):
        st.title("Sign In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Sign In"):
            with Session(self.engine) as session:
                user = session.exec(select(User).where(User.username == username)).first()
                if user and user.password == password:
                    st.session_state.user = user
                    self.user = user
                    st.success(f"Welcome, {user.name}!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")

    def signout(self):
        if st.button("Sign Out"):
            self.user = None
            st.session_state.user = None
            st.session_state.messages = []
            st.experimental_rerun()

    def signup_and_signin(self):
        with st.sidebar:
            selected = option_menu("ChatBot", ["Signin", 'Signup'],
                icons=['house', 'gear'], menu_icon="cast", default_index=0)

        if selected == "Signin":
            self.signin()

        elif selected == "Signup":
            self.signup()
