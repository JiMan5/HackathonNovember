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
    __name = ""
    __location = ""
    __date = datetime.datetime.now()
    __max_people = 0
    __discription = ""
    __max_words = 500
    __type_of_event = ""
    __is_open = False

    #creator = Creator()
    __users = [] * __max_people
    __num_of_users = 0

    def __init__(self, name, location, maxPeople, type, discription):
        self.__name = name
        self.__location = location
        self.__max_people = maxPeople
        self.__type_of_event = type
        self.set_discription(discription)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def set_date(self, day, month, year):
        self.__date = datetime.datetime(year, month, day)

    def get_date(self):
        return self.__date

    def set_max_people(self, maxPeople):
        self.__maxPeople = maxPeople

    def get_max_people(self):
        return self.__maxPeople

    def set_discription(self, discription):
        numOfWords = len(discription.split())
        #print(numOfWords)
        if numOfWords < self.__max_words:
            self.__discription = discription
        else:
            print('Write less words')

    def get_discription(self):
        return self.__discription

    def get_max_words(self):
        return self.__max_words
    
    def set_type(self, type):
        if type in Types:
            self.__type_of_event = type
        else:
            print('Type is not in the list')

    def get_type(self):
        return self.__type_of_event

    def open_event(self):
        self.__is_open = True

    def close_events(self):
        self.__is_open = False

    def is_open(self):
        return self.__is_open

    def show_event(self):
        print(self.__name)
        print(self.__location)
        print(self.__type_of_event)
        print(self.__date.strftime("%x"))
        print(self.__discription)
        if self.__is_open:
            print("Event is open")
        else:
            print("Event is carently closed")
        print()
    
    def add_user(self, user):
        self.__users[self.__num_of_users] = user
        self.__num_of_users = self.__num_of_users + 1

    def add_list_of_users(self, users):
        self.__users = users
        self.__num_of_users = len(self.__users)
    
    def get_users(self):
        self.__users

    def remove_user(self, user_index):
        self.__users.pop(user_index)
        self.__num_of_users = self.__num_of_users - 1
