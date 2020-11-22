class Event:
    name = ""
    location = ""
    date = ""
    maxPeople = 0
    description = ""
    maxWords = 500
    typeOfEvent = ""
    isOpen = False
    users = [] * maxPeople
    host = 0
    points = 0

    def __init__(self, name, location, date, maxPeople, type, description, host):
        self.name = name
        self.location = location
        self.date = date
        self.maxPeople = maxPeople
        self.typeOfEvent = type
        self.setDescription(description)
        self.host = host

    def setDescription(self, description):
        numOfWords = len(description.split())
        if numOfWords < self.maxWords:
            self.description = description
        else:
            print('Write less words')

    def openEvent(self):
        self.isOpen = True

    def closeEvent(self):
        self.isOpen = False

    def eventIsOpen(self):
        return self.isOpen

    def showEvent(self):
        print('Host: ' + self.host.username)
        print(self.name)
        print(self.location)
        print('max people: ' + str(self.maxPeople))
        print(self.typeOfEvent)
        print(self.date)
        print(self.description)
        if self.isOpen:
            print("Event is open")
        else:
            print("Event is currently closed")
        print()

    def isFull(self):
        return self.maxPeople == len(self.users)

    def addUser(self, user):
        if not self.isFull():
            self.users.append(user)

    def removeUser(self, user_index):
        if user_index > -1:
            self.users.pop(user_index)
