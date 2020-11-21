from Creator import Creator
from User import User

Description = "From the outside this house looks magnificent. It has been built with white bricks and has mahogany wooden decorations"

Types = [
    'programming','photos','painting','music','maths','literature','gaming','cooking','cine',
    'boardgame','basket','tennis','theater'
]

Users = [
    User("John", "John@gmail.com", "dscdc", 20, "Toumpa", Types[4]),
    User("Helen", "Helen@gmail.com", "fvdfv", 24, "Toumpa", Types[2]),
    User("Nick", "Nick@gmail.com", "dsccdsc", 21, "Toumpa", Types[2]),
    User("Ron", "Ron@gmail.com", "dscdcdsc", 20, "Toumpa", Types[1]),
    User("Paul", "Paul@gmail.com", "scsadwdsc", 19, "Toumpa", Types[6]),
    User("Emily", "Emily@gmail.com", "sxcdsc", 25, "Toumpa", Types[9]), 
    User("Rosa", "Rosa@gmail.com", "cvfdsc", 36, "Toumpa", Types[11]), 
    User("George", "George@gmail.com", "dcsadsc", 18, "Toumpa", Types[6])
]

Creators = [
    Creator("John", "John@gmail.com", "dscdsc", 24, "Toumpa", Types[4]),
    Creator("John", "John@gmail.com", "dscdsc", 28, "Toumpa", Types[2]),
    Creator("John", "John@gmail.com", "dscdsc", 21, "Toumpa", Types[8]),
    Creator("John", "John@gmail.com", "dscdsc", 20, "Toumpa", Types[6]),
    Creator("John", "John@gmail.com", "dscdsc", 21, "Toumpa", Types[4]),
    Creator("John", "John@gmail.com", "dscdsc", 23, "Toumpa", Types[9]),
    Creator("John", "John@gmail.com", "dscdsc", 29, "Toumpa", Types[11]),
    Creator("John", "John@gmail.com", "dscdsc", 18, "Toumpa", Types[9])
]

Events = [
    Creators[0].createEvent("party", "toumpa", "04/11/2020", 5, Types[4], Description),
    Creators[1].createEvent("superparty", "kalamaria", "04/11/2020", 5, Types[4], Description),
    Creators[2].createEvent("koronoparty", "xarilaou", "04/11/2020", 5, Types[4], Description),
    Creators[3].createEvent("sambaparty", "kentro", "04/11/2020", 5, Types[4], Description),
    Creators[4].createEvent("rooftop", "kalamaria", "04/11/2020", 5, Types[4], Description),
    Creators[5].createEvent("taraca babi", "thermi", "04/11/2020", 5, Types[4], Description),
    Creators[6].createEvent("lwl", "kentro", "04/11/2020", 5, Types[4], Description),
    Creators[7].createEvent("lwlparty", "toumpa", "04/11/2020", 5, Types[4], Description),
]

if __name__ == '__main__':
    creator = Creator("John", "John@gmail.com", "dscdsc", 20, "Toumpa", Types[4])

    creator.createEvent("party", "toumpa", "04/11/2020", 5, Types[4], Description)
    creator.events[0].openEvent()

    creator.invite(Users[2], creator.events[0])
    Users[2].acceptInvite(0)
    Users[3].joinEvent(creator.events[0])

    creator.events[0].showEvent()

    for i in range(0, len(creator.events[0].users)):
        print(creator.events[0].users[i].username)

    #add friends