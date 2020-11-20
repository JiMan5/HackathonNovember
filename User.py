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
    __username = ""
    __email = ""
    __password = ""
    __age = 0
    __location = ""
    __hobbies = [] #list of Types hobbies
    __friends = [] #list of users
    __score = 0
    __creator = False
    __Bookmarks = [] #list of events

    def __init__(username, email, password, age, location, self):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__age = age
        self.__location = location

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
    
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def add_hobby(self, hobby):
        self.__hobbies.append(hobby)

    def get_hobbies(self):
        return self.__hobbies

    def add_friend(self, friend):
        self.__friends.append(friend)

    def get_friends(self):
        return self.__friends

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_creator(self):
        self.__creator = True

    def is_creator(self):
        return self.__creator

    def add_bookmark(self, bookmark):
        self.__Bookmarks.append(bookmark)

    def get_bookmarks(self):
        return self.__Bookmarks
        

    