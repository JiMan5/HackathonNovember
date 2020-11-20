import os
from flask import Flask, request, render_template, render_template_string, session, url_for, jsonify, make_response
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import sql
from json import dumps
from flask_mail import Mail, Message
import json

app = Flask(__name__)

app.secret_key = 'hello'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dataBase = SQLAlchemy(app)

mail = Mail(app)


# app.config['MAIL_SERVER']='http://127.0.0.1:5000/'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '12345'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

class users(dataBase.Model):
    _id = dataBase.Column("id", dataBase.Integer, primary_key=True)
    username = dataBase.Column(dataBase.String(100))
    email = dataBase.Column(dataBase.String(100))
    password = dataBase.Column(dataBase.String(100))
    country = dataBase.Column(dataBase.String(100))
    city = dataBase.Column(dataBase.String(100))
    address = dataBase.Column(dataBase.String(100))
    dateOfBirth = dataBase.Column(dataBase.String(100))
    edu = dataBase.Column(dataBase.String(100))
    hobbies = dataBase.Column(dataBase.String(200))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.country = None
        self.city = None
        self.address = None
        self.dateOfBirth = None
        self.edu = None
        self.hobbies = None

    def add_second_data(self, country, city, address, dateOfBirth, edu):
        self.country = country
        self.city = city
        self.address = address
        self.dateOfBirth = dateOfBirth
        self.edu = edu

    def add_third_data(self, hobbies):
        self.hobbies = hobbies


# global users
# users = pd.DataFrame({'username':['example'],'email':['example@gmail.com'],'password':['1234']})

@app.route('/')
def index():
    return render_template('RegisterLogin.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = users.query.filter_by(username=username).first()
    if user:
        if user.password == password:

            return '11'

        else:

            return '10'

    else:

        return '00'


@app.route('/upload', methods=['POST'])
def upload():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    session.permanent = True
    session['username'] = username

    # msg = Message('Hello', sender='chrissiargas@gmail.com', recipients=[email])
    # msg.body = "This is the email body"
    # mail.send(msg)

    string = ''

    found_user = users.query.filter_by(username=username).first()
    if found_user:
        string += '0'

    else:
        string += '1'

    found_email = users.query.filter_by(email=email).first()
    if found_email:
        string += '0'

    else:
        string += '1'

    if string != '11':
        return string

    usr = users(username, email, password)
    dataBase.session.add(usr)
    dataBase.session.commit()

    return string


@app.route('/second_upload', methods=['POST'])
def second_upload():
    country = request.form.get('country')
    city = request.form.get('city')
    address = request.form.get('address')
    dateOfBirth = request.form.get('dateOfBirth')
    edu = request.form.get('edu')

    find_user = users.query.filter_by(username=session['username']).first()
    find_user.add_second_data(country, city, address, dateOfBirth, edu)
    dataBase.session.commit()


@app.route('/third_upload', methods=['POST'])
def third_upload():
    hobbies = request.form.get('hobbies')

    find_user = users.query.filter_by(username=session['username']).first()
    find_user.add_third_data(hobbies)
    dataBase.session.commit()


@app.route('/main_page')
def go_to_main_page():
    return render_template('main_page.html')


if __name__ == '__main__':
    dataBase.create_all()
    app.run(debug=True)
