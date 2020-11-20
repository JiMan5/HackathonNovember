class Event:
    name = ""
    location = ""
    date = ""
    max_people = 0
    description = ""
    max_words = 500
    type_of_event = ""
    is_open = False
    users = [] * max_people

    def __init__(self, name, location, date, maxPeople, type, description):
        self.name = name
        self.location = location
        self.date = date
        self.max_people = maxPeople
        self.type_of_event = type
        self.set_description(description)

    def set_description(self, description):
        numOfWords = len(description.split())
        if numOfWords < self.max_words:
            self.discription = description
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
        print(self.date)
        print(self.discription)
        if self.is_open:
            print("Event is open")
        else:
            print("Event is currently closed")
        print()

    #users
    def is_full(self):
        return self.max_people == len(self.users)

    def add_user(self, user):
        if not self.is_full():
            self.users.append(user)

    def remove_user(self, user_index):
        if user_index > -1:
            self.users.pop(user_index)
