from Event import Event

class Invite:
    username = ""
    email = ""
    event = Event("", "", "", 0, 0, "")

    def __init__(self, username, email, event):
        self.username = username
        self.email = email
        self.event = event