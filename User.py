import googlemaps

class Point:
    longitude = 0
    latitude = 0

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

def find_distance(point1, point2):
    gmaps = googlemaps.Client(key = 'YK-XhBhYj2hAxi_jVui1Fd4flbgIh-q_SKTjTZYW9J8')
    distance = gmaps.distance_matrix([str(point1.latitude) + " " + str(point1.longitude)],
                                     [str(point2.latitude) + " " + str(point2.longitude)], mode='walking')[
        'rows'][0]['elements'][0]
    return distance


point1 = Point(1, 2)
point2 = Point(131, 232)
print(find_distance(point1, point2))


class User:
    username = ""
    email = ""
    password = ""
    age = 0
    location = ""
    hobbies = [] #list of Types hobbies
    friends = [] #list of users
    friendRequests = []
    score = 0
    bookmarks = [] #list of events
    invites = []

    def __init__(self, username, email, password, age, location, hobbies, friends = [], bookmarks = []):
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
        self.invites[indexOfInvite].accept == True
        self.invites[indexOfInvite].event.addUser(self)
        self.invites.pop(indexOfInvite)

    def joinEvent(self, event):
        if event.eventIsOpen():
            self.bookmarks.append(event)
            event.addUser(self)

    def recommendEvents(self, events, filters = 0):
        pass
