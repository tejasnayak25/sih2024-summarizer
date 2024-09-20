from flask import Flask, send_file, request
import os
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_AI_API"])

app = Flask(__name__, "", "")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return send_file(os.path.join(os.getcwd(), "index.html"))

@app.post("/summarize")
def summarize():
    text = request.data.decode("utf-8")
    response = model.generate_content(f'Summarize: "{text}"')
    return response.text

def main():
    try:
        app.run(port=5000)
    except Exception as err:
        pass

if __name__ == "__main__":
    main()