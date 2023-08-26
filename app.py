from flask import Flask, render_template, request
import openai
# import pandas as pd
# import numpy as np
from getpass import getpass
from dotenv import load_dotenv #Import dotenv
import os


app = Flask(__name__)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#Make sure you install python, create a project environment, install flask
#Use python -m flask run to run, then click on link
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generate_response", methods=["POST"])
def generate_response():
    user_input = request.form["user_input"]

    #Use OpenAI to generate a response
    response = generate_ai_response(user_input)

    return render_template("index.html", user_input=user_input, response=response)

def generate_ai_response(user_input):
    if user_input == "Academic":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on how to deal with academic stress",
            max_tokens=100, 
        )
    elif user_input == "Personal":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on how to deal with personal stress",
            max_tokens=100,
        )
    else:
        return "N/A."
    return response.choices[0].text

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug=True)