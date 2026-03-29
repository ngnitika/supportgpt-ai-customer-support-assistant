from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Create app
app = FastAPI()

chat_history = []

def get_html(messages=[]):
    chat_html = ""

    for role, text in messages:
        formatted_text = text.replace("\n", "<br>")  # ✅ move here

        if role == "user":
            chat_html += f"""
            <div style="text-align:right; margi
            n:10px;">
                <div style="
                    display:inline-block;
                    background:#007bff;
                    color:white;
                    padding:10px;
                    border-radius:10px;
                    max-width:70%;
                    word-wrap:break-word;
                    white-space:pre-wrap;
                ">
                    {formatted_text}
                </div>
            </div>
            """
    else:
        chat_html += f"""
        <div style="text-align:left; margin:10px;">
            <div style="
                display:inline-block;
                background:#f1f1f1;
                padding:10px;
                border-radius:10px;
                max-width:70%;
                word-wrap:break-word;
                white-space:pre-wrap;
            ">
                {formatted_text}
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Chat Assistant</title>
    </head>
    <body style="font-family: Arial; background:#f9f9f9; padding:20px;">

        <h2>🤖 AI Chat Assistant</h2>

        <div style="max-width:600px; margin:auto;">
            {chat_html}
        </div>

        <form method="post" style="position:fixed; bottom:20px; width:100%; max-width:600px;">
            <input type="text" name="user_input" placeholder="Type your message..."
                style="width:70%; padding:10px;" required>

            <button type="submit"
                onclick="this.innerText='Thinking...'"
                style="padding:10px;">
                Send
            </button>
        </form>

    </body>
    </html>
    """


@app.get("/", response_class=HTMLResponse)
def home():
    print("HOME ROUTE HIT")
    return get_html(chat_history)


@app.post("/", response_class=HTMLResponse)
def generate(user_input: str = Form(...)):
    try:
        response = model.generate_content(user_input)
        response_text = response.text

    except Exception as e:

        response_text = f"Error: {str(e)}"

    chat_history.append(("user", user_input))
    chat_history.append(("ai", response_text))

    return get_html(chat_history)  