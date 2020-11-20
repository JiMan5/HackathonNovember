from Event import Event

class Invite:
    username = ""
    email = ""
    event = Event("", "", "", 0, 0, "")
    accept = False

    def __init__(self, username, email, event, accept):
        self.username = username
        self.email = email
        self.event = event
        self.accept = accept