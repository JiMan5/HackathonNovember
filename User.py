from FriendRequest import FriendRequest


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

    def joinEvent(self, event):
        if event.eventIsOpen():
            self.bookmarks.append(event)
            event.addUser(self)

    def addFriendrequest(self, friendRequest):
        self.friendRequests.append(friendRequest)

    def sendFriendRequest(self, user):
        friendRequest = FriendRequest(self, user)
        user.addFriendrequest(friendRequest)

    def addFriend(self, user):
        self.friends.append(user)

    def acceptFriendRequest(self, indexOfFriendReq):
        friendRequest = self.friendRequests[indexOfFriendReq]
        friendRequest.accept == True
        self.addFriend(friendRequest.user1)
        friendRequest.user1.addFriend(friendRequest.user2)


    
