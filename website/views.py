from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/academic')
def academic():
    return render_template('academic.html')

@views.route('/family')
def family():
    return render_template('family.html')

@views.route('/personal')
def personal():
    return render_template('personal.html')

@views.route('/social')
def social():
    return render_template('social.html')