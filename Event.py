import datetime

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

class Event:
    name = ""
    location = ""
    date = datetime.datetime.now()
    max_people = 0
    discription = ""
    max_words = 500
    type_of_event = ""
    is_open = False
    users = [] * max_people
    #__creator = Creator()

    def __init__(self, name, location, maxPeople, type, discription):
        self.name = name
        self.location = location
        self.max_people = maxPeople
        self.type_of_event = type
        self.set_discription(discription)

    def set_date(self, day, month, year):
        self.date = datetime.datetime(year, month, day)

    def set_discription(self, discription):
        numOfWords = len(discription.split())
        #print(numOfWords)
        if numOfWords < self.max_words:
            self.discription = discription
        else:
            print('Write less words')

    def open_event(self):
        self.is_open = True

    def close_event(self):
        self.is_open = False

    def is_open(self):
        return self.is_open

    def show_event(self):
        print(self.name)
        print(self.location)
        print('max people: ' + str(self.max_people))
        print(self.type_of_event)
        print(self.date.strftime("%x"))
        print(self.discription)
        if self.is_open:
            print("Event is open")
        else:
            print("Event is currently closed")
        print()

    #users
    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_index):
        if user_index > -1:
            self.users.pop(user_index)
