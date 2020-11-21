import math


Locations = {
    "Kalamaria": [40.57, 22.95],
    "Thermi": [40.54, 23.02],
    "Kentro": [40.64, 22.93],
    "Toumpa": [40.61, 22.97],
    "Evosmos": [40.67, 22.91],
    "Sykies": [40.64, 22.95],
    "Pylaia": [40.59, 22.99],
    "Triandria": [40.62, 22.97]
}


def findDistance(p1, p2):
    r = 6371
    x1 = r * math.sin(p1[0]) * math.cos(p1[1])
    y1 = r * math.sin(p1[0]) * math.sin(p1[1])
    x2 = r * math.sin(p2[0]) * math.cos(p2[1])
    y2 = r * math.sin(p2[0]) * math.sin(p2[1])

    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance / 100


def calculatePoints(distance, sameType, ageDifference, maxPeople):
    return (-distance) * 0.3 + sameType * 0.3 + ageDifference * 0.25 + maxPeople * 0.15


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

    def recommendEvents(self, allEvents, types=[], dates=[], maxPeople=[], locations=[]):
        events = []
        for i in range(0, len(allEvents)):
            if allEvents[i].typeOfEvent in types:
                events.append(allEvents[i])
            if allEvents[i].date in dates:
                events.append(allEvents[i])
            if allEvents[i].maxPeople in maxPeople:
                events.append(allEvents[i])
            if allEvents[i].location in locations:
                events.append(allEvents[i])

        for i in range(0, len(events)):
            distance = findDistance(Locations.get(self.location), Locations.get(events[i].location))
            sameType = 0
            if events[i].typeOfEvent in self.hobbies:
                sameType = 1
            ageDifference = self.age - events[i].host.age
            if ageDifference < 0:
                ageDifference = -ageDifference
                agePoints = 0
            if ageDifference < 5:
                agePoints = 1
            elif ageDifference < 10:
                agePoints = 0.5
            maxPeople = 0
            if events[i].maxPeople - len(events[i].users) > 10:
                maxPeople = 1
            elif events[i].maxPeople - len(events[i].users) > 5:
                maxPeople = 0.5

            events[i].points = calculatePoints(distance, sameType, agePoints, maxPeople)

        events.sort(key=lambda x: x.points, reverse=True)

        for i in range(0, len(events)):
            print(events[i].name + str(events[i].points))