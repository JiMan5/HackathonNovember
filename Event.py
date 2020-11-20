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
    #Creator creator = Creator()
    __location = ""
    __date = datetime.datetime.now()
    __maxPeople = 0
    __discription = ""
    __maxWords = 500
    __typeOfEvent = ""
    __isOpen = False

    #print(date.strftime("%x"))

    def __init__(self, name, location, maxPeople, type):
        self.__name = name
        self.__location = location
        self.__maxPeople = maxPeople
        self.__typeOfEvent = type

    def setname(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setLocation(self, location):
        self.__location = location

    def getLocation(self):
        return self.__location

    def setDate(self, day, month, year):
        self.__date = datetime.datetime(year, month, day)

    def getDate(self):
        return self.__date

    def setMaxPeople(self, maxPeople):
        self.__maxPeople = maxPeople

    def getMaxPeople(self):
        return self.__maxPeople

    def setDiscription(self, discription):
        numOfWords = len(discription.split())
        #print(numOfWords)
        if numOfWords < self.__maxWords:
            self.__discription = discription
        else:
            print('Write less words')

    def getDiscription(self):
        return self.__discription

    def getMaxWords(self):
        return self.__maxWords
    
    def setType(self, type):
        if type in Types:
            self.__typeOfEvent = type
        else:
            print('Type is not in the list')

    def getType(self):
        return self.__typeOfEvent

    def activateEvent(self):
        self.__isOpen = True

    def isOpen(self):
        return self.__isOpen

    def showEvent(self):
        print(self.__name)
        print(self.__location)
        print(self.__typeOfEvent)
        print(self.__date.strftime("%x"))
        print(self.__discription)
        if self.__isOpen:
            print("Event is open")
        else:
            print("Event is carently closed")
        print()
    

    
