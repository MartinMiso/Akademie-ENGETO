"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Mišo
email: martin.miso@seznam.cz
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2]

# print(text_1)
# print()
# print(text_2)
# print()
# print(text_3)

# user |   password  |
# +------+-------------+
# | bob  |     123     |
# | ann  |   pass123   |
# | mike | password123 |
# | liz  |   pass123

# users and passwords
users = {"bob" : "123",
        "ann" : "pass123",
        "mike" : "password123",
        "liz" : "pass123"}
user_register = ()

# password verify
def enter():
    name = input("User name: ")#.lower() - případné ověření malých písmen
    password = input("Your password: ")#.lower()

    if users.get(name) == password:
        user_register = True
        print("Welcome to the web")
            
    else:
        print("Sorry, you must go out!")
        


enter()

if user_register:
    print("Jsi registrovaný")