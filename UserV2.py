from Invite import Invite

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

class User:
    username = ""
    email = ""
    password = ""
    age = 0
    location = ""
    hobbies = [] #list of Types hobbies
    friends = [] #list of users
    score = 0
    eventsToAttend = [] #events that he hasn't attended yet
    eventsAttended = [] #events that has already attended
    bookmarks = [] #list of events
    invites = [] 

    def __init__(self, username, email, password, age, location, hobbies, friends, bookmarks, toattend, attended):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.location = location
        self.hobbies = hobbies
        self.friends = friends
        self.bookmarks = bookmarks
        self.eventsToAttend = toattend
        self.eventsAttended = attended

    def setInvite(self, username, email, event):
        invites.append(Invite(self, username, email, event))
        

    
