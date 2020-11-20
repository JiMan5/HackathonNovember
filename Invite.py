#from Creator import Creator
#from Event import Event

class Invite:
    creator = 0
    event = 0
    accept = False

    def __init__(self, creator, event):
        self.creator = creator
        self.event = event
        self.accept = False