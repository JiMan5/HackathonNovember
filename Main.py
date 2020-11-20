from User import User
from Event import Event

Discription = "From the outside this house looks magnificent. It has been built with white bricks and has mahogany wooden decorations"


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

Users = [
    User("dsfds", "dscdsc", "dscdsc", 4, "sdfsc"),
    User("dsfds", "dscdsc", "dscdsc", 5, "sdfsc"), 
    User("dsfds", "dscdsc", "dscdsc", 6, "sdfsc"), 
    User("dsfds", "dscdsc", "dscdsc", 7, "sdfsc")
]

if __name__ == '__main__':
    event = Event("party", "toumpa", "04/11/2020", 5, Types[4], Discription)

    event.show_event()

    event.open_event()
    event.show_event()

    for i in range(0, 4):
        event.add_user(Users[0])

    print(event.users)
    event.remove_user(1)

    print(event.users)