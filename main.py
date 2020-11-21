from Creator import Creator
from User import User, findDistance

Description = "From the outside this house looks magnificent." \
              " It has been built with white bricks and has mahogany wooden decorations"

Types = [
    'programming', 'photos', 'painting', 'music', 'maths', 'literature', 'gaming', 'cooking', 'cine',
    'boardgame', 'basket', 'tennis', 'theater'
]

Locations = {
    "Kalamaria": [40.57, 22.95],
    "Thermi": [40.54, 23.02],
    "Kentro": [40.64, 22.93],
    "Toumpa": [40.61, 22.97],
    "Evosmos": [40.67, 22.91],
    "Sykies": [40.64, 22.95],
    "Pylaia": [40.59, 22.99],
    "Triandria": [40.62, 22.97]
}

Users = [
    User("John", "John@gmail.com", "dscdc", 20, "Toumpa", Types[4]),
    User("Helen", "Helen@gmail.com", "fvdfv", 24, "Thermi", Types[2]),
    User("Nick", "Nick@gmail.com", "dsccdsc", 21, "Triandria", Types[2]),
    User("Ron", "Ron@gmail.com", "dscdcdsc", 20, "Sykies", Types[1]),
    User("Paul", "Paul@gmail.com", "scsadwdsc", 19, "Toumpa", Types[6]),
    User("Emily", "Emily@gmail.com", "sxcdsc", 25, "Kentro", Types[9]),
    User("Rosa", "Rosa@gmail.com", "cvfdsc", 36, "Kentro", Types[11]),
    User("George", "George@gmail.com", "dcsadsc", 18, "Thermi", Types[6])
]

Creators = [
    Creator("Helen", "John@gmail.com", "dscdsc", 24, "Toumpa", Types[4]),
    Creator("John", "John@gmail.com", "dscdsc", 28, "Thermi", Types[2]),
    Creator("Helen", "John@gmail.com", "dscdsc", 21, "Kentro", Types[8]),
    Creator("Rosa", "John@gmail.com", "dscdsc", 20, "Thermi", Types[6]),
    Creator("John", "John@gmail.com", "dscdsc", 21, "Toumpa", Types[4]),
    Creator("John", "John@gmail.com", "dscdsc", 23, "Thermi", Types[9]),
    Creator("George", "John@gmail.com", "dscdsc", 29, "Thermi", Types[11]),
    Creator("George", "John@gmail.com", "dscdsc", 18, "Kentro", Types[9])
]

Events = [
    Creators[0].createEvent("party", "Toumpa", "06/11/2020", 5, Types[5], Description),
    Creators[1].createEvent("superparty", "Kalamaria", "04/11/2020", 20, Types[4], Description),
    Creators[2].createEvent("koronoparty", "Xarilaou", "08/11/2020", 15, Types[8], Description),
    Creators[3].createEvent("sambaparty", "Kentro", "02/11/2020", 30, Types[9], Description),
    Creators[4].createEvent("rooftop", "Kalamaria", "15/11/2020", 4, Types[2], Description),
    Creators[5].createEvent("taraca babi", "Thermi", "15/11/2020", 17, Types[0], Description),
    Creators[6].createEvent("lwl", "Kentro", "02/11/2020", 5, Types[11], Description),
    Creators[7].createEvent("lwlparty", "Toumpa", "04/11/2020", 8, Types[9], Description)
]

if __name__ == '__main__':
    print(Locations.get("Toumpa"))
    print(Locations["Toumpa"])

    distance = findDistance(Locations["Toumpa"], Locations["Kalamaria"])
    print("Distance: " + str(distance))

    creator = Creator("John", "John@gmail.com", "dscdsc", 20, "Toumpa", Types[4])

    creator.createEvent("party", "toumpa", "04/11/2020", 5, Types[4], Description)
    creator.events[0].openEvent()

    creator.invite(Users[2], creator.events[0])
    Users[2].acceptInvite(0)
    Users[3].joinEvent(creator.events[0])

    creator.events[0].showEvent()

    for i in range(0, len(creator.events[0].users)):
        print(creator.events[0].users[i].username)