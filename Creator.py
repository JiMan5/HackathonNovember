from User import User
from Event import Event

class Creator(User):

    events = []     # array of Events
    invites = []    # array containing the invited Users 

    def __init__(self, username, email, password, age, location, hobbies, friends, bookmarks):
        super().__init__(username, email, password, age, location, hobbies, friends, bookmarks)

    def createEvent(self, name, location, date, maxPeople, type, description):
        myEvent = Event(self, name, location, date, maxPeople, type, description)
        events.append(myEvent)

    def invite(self, user, event):
        invites.append(user)
        user.setInvite(self, username, email, event)
    

