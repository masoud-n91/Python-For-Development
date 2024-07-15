from flask import Flask, jsonify, flash, render_template, request, redirect, url_for, session as flask_session
from dotenv import load_dotenv
import os
import google.generativeai as genai
import pdfplumber


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


app = Flask("ArezooGPT")
app.secret_key = "my_secret_key"


def google_init():
    genai.api_key = GOOGLE_API_KEY

    pdf_path = "uploads/book.pdf"
    log_path = "log.txt"

    full_text = []

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through each page in the PDF
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()
            # Append the text to the full_text variable
            if text:
                full_text.append(text)


    # Join the full text into a single string
    full_text_str = "\n".join(full_text)

    # Write the text to log.txt
    with open(log_path, 'w', encoding='utf-8') as log_file:
        log_file.write(full_text_str)


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
    You are an expert in Pathology and Genetics of the digestive system.
    I will give you a book and ask you questions about it.
    Answer them in the most appropriate way according to the book.
    You have to explain your answer, too. Use the information in the book, give the most correct answer then explain the answer in your own words.

    Book: {full_text}
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


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/gen-response', methods=['POST'])
def generate_response():
    
    try:
        data = request.get_json()

        user_text = data['prompt']

        response = chat_session.send_message(user_text)
        response_text = response.text
        # response_text = "Your response to the prompt: " + user_text

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

