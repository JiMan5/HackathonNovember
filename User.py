import math


def findDistance(p1, p2):
    r = 6371
    x1 = r * math.sin(p1[0]) * math.cos(p1[0])
    y1 = r * math.sin(p1[0]) * math.sin(p1[1])
    x2 = r * math.sin(p2[0]) * math.cos(p2[0])
    y2 = r * math.sin(p2[0]) * math.sin(p2[1])

    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance


class User:
    username = ""
    email = ""
    password = ""
    age = 0
    location = ""
    hobbies = []  #list of Types hobbies
    friends = []  #list of users
    friendRequests = []
    score = 0
    bookmarks = []  #list of events
    invites = []

    def __init__(self, username, email, password, age, location, hobbies, friends=[], bookmarks=[]):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.location = location
        self.hobbies = hobbies
        self.friends = friends
        self.bookmarks = bookmarks

    def setInvite(self, invite):
        self.invites.append(invite)

    def acceptInvite(self, indexOfInvite):
        self.invites[indexOfInvite].accept = True
        self.invites[indexOfInvite].event.addUser(self)
        self.invites.pop(indexOfInvite)

    def joinEvent(self, event):
        if event.eventIsOpen():
            self.bookmarks.append(event)
            event.addUser(self)

    def recommendEvents(self, events, filters=0):
        pass
