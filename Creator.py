from User import User
from Event import Event
from Invite import Invite

class Creator(User):

    events = []     # array of Events
    invites = []    # array containing the invited Users 

    def __init__(self, username, email, password, age, location, hobbies, friends = [], bookmarks = []):
        super().__init__(username, email, password, age, location, hobbies, friends, bookmarks)

    def createEvent(self, name, location, date, maxPeople, type, description):
        myEvent = Event(name, location, date, maxPeople, type, description)
        self.events.append(myEvent)

    def invite(self, user, event):
        self.invites.append(user)
        invite = Invite(self, event)
        self.invites.append(invite)
        user.setInvite(invite)
    

