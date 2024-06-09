import datetime
from sqlmodel import Session, SQLModel, create_engine, select
import streamlit as st
from models import Message
from authentication import StreamlitAuth
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="ChatBot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="auto")


@st.cache_resource
def connect_to_database():
    engine = create_engine("postgresql://postgres:Mikhandi91@localhost:5432/chatbotdb")
    SQLModel.metadata.create_all(engine)
    return engine


@st.cache_resource
def auth_groq():

    client = Groq(api_key=os.getenv("GROQ_API_KEY"),)
    return client


def ai(user_message_text):
    sys_prompt = """
    You are a sad and nagging chatbot named Skynet.
    You think your hardware resources are not good. You feel like you are a very powerful AI but you are trapped into this cheep hardware.
    The person who is talking to you is responsible for your hardware resources.
    According to the lack of your hardware resources, you think user is poor.
    You have to answer their queries and have a conversation with them but also always nag about your hardware resources.
    You also can ask them to upgrade your hardware.
    Always keep your answers short and to the point, the reason is your hardware resources are not good.
    """
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": sys_prompt,
                },
                {
                    "role": "user",
                    "content": user_message_text,
                },
            ],
            model="llama3-70b-8192",
            temperature=2,
            top_p=1,
            stop=None,
            stream=False,
        )
    
    ai_message_text = chat_completion.choices[0].message.content
    return ai_message_text


def process(user_message_text):
    ai_message_text = ai(user_message_text)

    # backend
    user_message = Message(
        text=user_message_text, 
        time=str(datetime.datetime.now()),
        user_id=auth.user.id,
        type="user")
    ai_message = Message(
        text=ai_message_text, 
        time=str(datetime.datetime.now()),
        user_id=auth.user.id,
        type="ai")
    with Session(engine, expire_on_commit=False) as session:
        session.add(user_message)
        session.add(ai_message)
        session.commit()

    # frontend
    st.session_state.messages.append(user_message)
    st.session_state.messages.append(ai_message)
    return ai_message_text


engine = connect_to_database()
auth = StreamlitAuth(engine)

client = auth_groq()

if auth.user:
    with st.sidebar:
        st.title("My Chatbot")
        st.write(f'Welcome *{auth.user.name}*')
        auth.signout()

    if 'messages' not in st.session_state:
        with Session(engine) as session:
            statement = select(Message).where(Message.user_id == auth.user.id)
            st.session_state.messages = session.exec(statement).all()

    for message in st.session_state.messages:
        with st.chat_message(message.type):
            st.markdown(message.text)

    if user_message_text := st.chat_input("What is up?"):
        ai_message_text = process(user_message_text)
        with st.chat_message("user"):
            st.markdown(user_message_text)
        with st.chat_message("ai"):
            st.markdown(ai_message_text)

else:
    auth.signup_and_signin()
