from website import create_app, render_template, request
import openai
# import pandas as pd
# import numpy as np
from getpass import getpass
from dotenv import load_dotenv #Import dotenv
import os

app = create_app()

#Enable debug mode, type python app.py
app.debug=True

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#Make sure you install python, create a project environment, install flask
#Use python -m flask run to run, then click on link
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/")

#Academic Advice
@app.route("/generate_response", methods=["POST"])
def generate_response():
    user_input = request.form["user_input"]

    #Use OpenAI to generate a response
    response = generate_ai_response(user_input)

    if user_input in ["Study Habits", "Academic Pressure", "Failure"]:
        page = "academic.html"
    elif user_input == "Communication":
        page = "family.html"
    elif user_input in ["Self-Esteem", "Body Image", "Identity"]:
        page = "personal.html"
    elif user_input in ["Friendships", "Peer Pressure", "Loneliness"]:
        page = "social.html"
    else:
        return "N/A."

    return render_template(page, user_input=user_input, response=response)

def generate_ai_response(user_input):
    if user_input == "Study Habits":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with academic stress and creating study habits",
            max_tokens=100, 
        )
    elif user_input == "Academic Pressure":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with academic stress and academic pressure",
            max_tokens=100,
        )
    elif user_input == "Failure":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with academic stress and failure",
            max_tokens=100,
        )
    elif user_input == "Communication":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with family stress and improving communication with them",
            max_tokens=100,
        )
    elif user_input == "Self-Esteem":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with personal stress and self-esteem",
            max_tokens=100,
        )
    elif user_input == "Body Image":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with personal stress and body image",
            max_tokens=100,
        )
    elif user_input == "Identity":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with personal stress and identity",
            max_tokens=100,
        )
    elif user_input == "Friendships":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with social stress and friendships",
            max_tokens=100,
        )
    elif user_input == "Peer Pressure":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with social stress and peer pressure",
            max_tokens=100,
        )
    elif user_input == "Loneliness":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="give advice on dealing with social stress and loneliness",
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