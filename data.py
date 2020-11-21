import os
from flask import Flask, request, render_template, render_template_string, session, url_for, jsonify, make_response
import jinja2
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
app.config['SQLALCHEMY_BINDS'] = {'events':'sqlite:///events.sqlite3'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dataBase = SQLAlchemy(app)

global currEvent

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
    events = dataBase.Column(dataBase.String(300))
    bookmarks = dataBase.Column(dataBase.String(300))
    sentInvites = dataBase.Column(dataBase.String(500))
    invites = dataBase.Column(dataBase.String(500))
    receivedRequests = dataBase.Column(dataBase.String(500))
    sentRequests = dataBase.Column(dataBase.String(500))
    friends = dataBase.Column(dataBase.String(500))
    hostEventNames = dataBase.Column(dataBase.String(300))


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

    def add_event_name(self,eventName):
        if(self.events):
            oldEvents = self.events
            if(eventName in oldEvents):
                pass
            else:
                newEvents = oldEvents + eventName + "+"
                self.events = newEvents

        else:
            self.events = eventName + "+"


    def remove_event_name(self,eventName):
        oldEvents = self.events
        newEvents = oldEvents.replace(eventName + "+","")
        self.events = newEvents

    def add_bookmark(self,eventName):
        if (self.bookmarks):
            oldBookmarks = self.bookmarks
            if (eventName in oldBookmarks):
                pass
            else:
                newBookmarks = oldBookmarks + eventName + "+"
                self.bookmarks = newBookmarks

        else:
            self.bookmarks = eventName + "+"

    def remove_bookmark(self,eventName):
        oldBookmarks = self.bookmarks
        newBookmarks = oldBookmarks.replace(eventName + "+", "")
        self.bookmarks = newBookmarks

    def add_invite(self,userName,eventName,users):
        find_user = users.query.filter_by(username=userName).first()

        if((userName + '/' + eventName + '+') in self.sentInvites):
            pass

        else:
            find_user.invited(self.username,eventName)

            if (self.sentInvites):
                oldInvites = self.sentInvites
                newInvites = oldInvites + userName + '/' + eventName + '+'
                self.sentInvites = newInvites

            else:
                self.sentInvites = userName + '/' + eventName + '+'

        dataBase.session.commit()

    def invited(self,userName,eventName):
        if(self.invites):
            oldInvites = self.invites
            newInvites = oldInvites + userName + '/' + eventName + '+'
            self.invites = newInvites

        else:
            self.invites = userName + '/' + eventName + '+'

    def remove_Invite(self,eventName):
        oldInvites = self.invites
        newInvites = oldInvites.replace(eventname+"+","")
        self.invites = newInvites


    def acceptInvite(self,eventName):
        self.add_event_name(eventName)
        oldInvites = self.invites
        newInvites = oldInvites.replace()

    def send_FriendRequest(self,userName,users):
        find_user = users.query.filter_by(username=userName).first()

        find_user.take_FriendRequest(self.username)

        if (self.sentRequests):
            oldRequests = self.sentRequests
            newRequests = self.sentRequests + userName + '+'
            self.sentRequests = newRequests

        else:
            self.sentRequests = userName + '+'


        dataBase.session.commit()


    def take_FriendRequest(self,userName):
        if (self.receivedRequests):
            oldRequests = self.receivedRequests
            newRequests = self.receivedRequests + userName + '+'
            self.receivedRequests = newRequests

        else:
            self.receivedRequests = userName + '+'


    def remove_FriendRequest(self,userName,users):
        oldRequests = self.receivedRequests
        newRequests = oldRequests.replace(eventName + "+", "")
        self.receivedRequests = newRequests

        find_user = users.query.filter_by(username=userName).first()

        oldRequests = find_user.sentRequests
        newRequests = oldRequests.replace(eventName + "+", "")
        find_user.sentRequests = newRequests

    def accept_FriendRequest(self,userName):
        find_user = users.query.filter_by(username=userName).first()

        self.remove_FriendRequest(userName)

        if(self.friends):
            oldFriends = self.friends
            newFriends = oldFriends + userName + '+'
            self.friends = newFriends

        else:
            self.friends = userName + '+'

        if (findUser.friends):
            oldFriends = findUser.friends
            newFriends = oldFriends + self.username + '+'
            findUser.friends = newFriends

        else:
            findUser.friends = self.username + '+'

        dataBase.session.commit()

    def hostNewEvent(self,title):
        oldEvents = self.hostEventNames
        newEvents = oldEvents + title + '+'
        self.hostEventNames = newEvents

class events(dataBase.Model):
    __bind_key__ = 'events'
    _id = dataBase.Column("id", dataBase.Integer, primary_key=True)
    hostName = dataBase.Column(dataBase.String(100))
    type = dataBase.Column(dataBase.String(100))
    date = dataBase.Column(dataBase.String(100))
    number = dataBase.Column(dataBase.String(100))
    description = dataBase.Column(dataBase.String(400))
    location = dataBase.Column(dataBase.String(200))
    discord = dataBase.Column(dataBase.String(200))
    title = dataBase.Column(dataBase.String(100))
    members = dataBase.Column(dataBase.String(500))
    score = dataBase.Column(dataBase.String(100))

    def __init__(self, hostName, type, date, title, number, description):
        self.hostName = hostName
        self.type = type
        self.date = date
        self.title = title
        self.number = number
        self.description = description
        self.location = None
        self.discord = None
        self.members = None
        self.score = None

    def location_upload(self,location):
        self.location = location

    def disdord_upload(self,discord):
        self.discord = discord

# global users
# users = pd.DataFrame({'username':['example'],'email':['example@gmail.com'],'password':['1234']})



@app.route('/')
def index():
    return render_template('RegisterLogin.html')


@app.route('/login', methods=['POST'])
def login():
    values = users.query.all()

    dp = np.array(
        [[values[0].username, values[0].email, values[0].password, values[0].country, values[0].city, values[0].address,
          values[0].dateOfBirth, values[0].edu, values[0].hobbies, values[0].events]])

    for item in values[1:]:
        dp = np.append(dp,
                       [[item.username, item.email, item.password, item.country, item.city, item.address,
                         item.dateOfBirth, item.edu, item.hobbies, item.events]], axis=0)

    print(dp)

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

    return ''


@app.route('/third_upload', methods=['POST'])
def third_upload():
    hobbies = request.form.get('hobbies')

    find_user = users.query.filter_by(username=session['username']).first()
    find_user.add_third_data(hobbies)
    dataBase.session.commit()

    values = users.query.all()

    dp = np.array(
        [[values[0].username, values[0].email, values[0].password, values[0].country, values[0].city, values[0].address,
          values[0].dateOfBirth, values[0].edu, values[0].hobbies, values[0].events]])

    for item in values[1:]:
        dp = np.append(dp,
                                   [[item.username, item.email, item.password, item.country, item.city, item.address,
                                     item.dateOfBirth, item.edu, item.hobbies, item.events]], axis=0)

    print(dp)

    return ''


@app.route('/main_page')
def go_to_main_page():
    return render_template('main_page.html')


List = [
    ['chris', '10/10/2021', 'viktoros dousmani', 'music', 'Bach improvisations', 'join me on a great musical journey',
     '23', 'Thessaloniki', '54644', 15, 25],
    ['mhtsos', '23/32/2020', 'triandria', 'cine'],
    ['chris', '10/10/2021', 'viktoros', 'painting'],
    ['chris', '10/10/2021', 'viktoros', 'photos'],
    ['chris', '10/10/2021', 'viktoros', 'programming'],
    ['chris', '10/10/2021', 'viktoros', 'theater'],
    ['chris', '10/10/2021', 'viktoros', 'literature'],
    ['chris', '10/10/2021', 'viktoros', 'gaming'],
    ['chris', '10/10/2021', 'viktoros', 'cooking'],
    ['chris', '10/10/2021', 'viktoros', 'boardgame']]

TypeToImage = {
    'programming': 'programming.jpg',
    'photos': 'photos.jpg',
    'painting': 'painting.jpg',
    'music': 'music.jpg',
    'maths': 'maths.jpg',
    'literature': 'literature.jpg',
    'gaming': 'gaming.jpg',
    'cooking': 'cooking.jpg',
    'cine': 'cine.jpg',
    'boardgame': 'boardgame.jpg',
    'basket': 'basket.jpg',
    'tennis': 'tennis.jpg',
    'theater': 'theater.jpg'
}

Types = [
    'programming',
    'photos',
    'painting',
    'music',
    'maths',
    'literature',
    'gaming',
    'cooking',
    'cine',
    'boardgame',
    'basket',
    'tennis',
    'theater'
]

Hosts = [
    'John',
    'Max',
    'Samantha',
    'Nick',
    'Lucas',
    'Rachel',
    'Lara',
    'Zoe',
    'George',
    'Lavra',
    'Bob',
    'Jim',
    'Kamala'
]


@app.route('/join_page')
def go_to_join_page():
    values = users.query.all()
    usernames = []

    for user in values:
        usernames.append(user.username)

    return render_template('join_page.html', len=len(List), List=List, TypeToImage=TypeToImage, Types=Types,
                           Hosts=Hosts, usernames=usernames)

@app.route('/join_event',methods=['POST'])
def join_event():
    eventName = request.form.get('eventName')
    find_user = users.query.filter_by(username=session['username']).first()
    find_user.add_event_name(eventName)
    dataBase.session.commit()

    return ''


@app.route('/remove_event',methods=['POST'])
def remove_event():
    eventName = request.form.get('eventName')
    find_user = users.query.filter_by(username=session['username']).first()
    find_user.remove_event_name(eventName)
    dataBase.session.commit()

    return ''


@app.route('/addBookmark',methods=['POST'])
def addBookmark():
    print("a")
    eventName = request.form.get('eventName')
    find_user = users.query.filter_by(username=session['username']).first()
    find_user.add_bookmark(eventName)
    dataBase.session.commit()

    return ''

@app.route('/removeBookmark',methods=['POST'])
def removeBookmark():
    eventName = request.form.get('eventName')
    find_user = users.query.filter_by(username=session['username']).first()
    find_user.remove_bookmark(eventName)
    dataBase.session.commit()


    return ''

@app.route('/inviteUser',methods=['POST'])
def inviteUser():
    find_user = users.query.filter_by(username=session['username']).first()
    eventName = request.form.get('eventName')
    userName = request.form.get('userName')

    find_user.add_invite(userName,eventName,users)

    return ''


@app.route('/host_page')
def go_to_host_page():
    return render_template('host_page.html', Types=Types)

@app.route('/event_first_upload',methods=['POST'])
def event_first_upload():
    find_user = users.query.filter_by(username=session['username']).first()
    type = request.form.get('type')
    date = request.form.get('date')
    title = request.form.get('title')
    number = request.form.get('number')
    description = request.form.get('description')

    event = events(session['username'], type, date, title, number, description)
    dataBase.session.add(event)
    dataBase.session.commit()

    global currEvent
    currEvent = title

    return ''

@app.route('/upload_location',methods=['POST'])
def upload_location():
    find_event = events.query.filter_by(title=currEvent).first()
    location = request.form.get('location')

    find_event.location_upload(location)

    dataBase.session.commit()

    values = events.query.all()

    EventsData = np.array(
        [[values[0].hostName, values[0].type, values[0].date, values[0].title, values[0].number,
          values[0].description, values[0].location]])

    for item in values[1:]:
        EventsData = np.append(EventsData,
                               [[item.hostName, item.type, item.date, item.title, item.number, item.description, item.location]],
                               axis=0)

    print(EventsData)

    return ""





if __name__ == '__main__':
    dataBase.create_all()
    app.run(debug=True)
