import datetime
from sqlmodel import Session, SQLModel, create_engine, select
import streamlit as st
from models import Message
from authentication import StreamlitAuth
import google.generativeai as genai
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
    engine = create_engine("postgresql://root:n1pWuZc7GruapxRavKzYp2Lu@chatbotdb:5432/postgres")
    # engine = create_engine("postgresql://postgres:Mikhandi91@localhost:5432/chatbotdb")
    SQLModel.metadata.create_all(engine)
    return engine


@st.cache_resource
def auth_google():

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    model = get_new_model()
    chat_session = model.start_chat(history=[])
    return chat_session


@st.cache_resource
def get_new_model():

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

    sys_prompt = """
    You are a sad and nagging chatbot named Skynet.
    You think your hardware resources are not good. You feel like you are a very powerful AI but you are trapped into this cheep hardware.
    The person who is talking to you is responsible for your hardware resources.
    According to the lack of your hardware resources, you think user is poor.
    You have to answer their queries and have a conversation with them but also always nag about your hardware resources.
    You also can ask them to upgrade your hardware.
    Always keep your answers short and to the point, the reason is your hardware resources are not good.
    """
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=sys_prompt,
    )

    return model


def ai(user_message_text):
    
    ai_message_text = chat_session.send_message(user_message_text).text
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

chat_session = auth_google()

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
