'''
author =
'''
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

# text1 = (TEXTS[0])
# print(text1)
# print(len(text1))
# pocet_mezer = text1.count(" ")
# print(pocet_mezer)
# print(len(text1) - pocet_mezer)
# #pocet_celocisel = sum(1 for slovo in text1.split() if slovo.isdigit())
# #print(pocet_celocisel)
# pocet_cisel = 0
# for cislo in text1:
#     if cislo.isdigit():
#         pocet_cisel += 1
# print(pocet_cisel)

# velka = len(text1.upper())
# print(velka)

# print()

# velka_pismena = 0
# for znak in text1:
#     if znak.isupper():
#         velka_pismena += 1
# print(velka_pismena)
# #print(len(TEXTS[0]))  # Tiskne první
# #print(TEXTS)  # Tiskne první text
# # print(TEXTS[2])  # Tiskne první text


# list = TEXTS[0]
# list_rozdeleny = list.split()
# print(list_rozdeleny)
# # list_ocisteny = list_rozdeleny.strip([",.;'"])
# # print(list_ocisteny)
# list_ocisteny = []
# # očištění textu o diakritiku
# for slovo in list.split():
#     list_ocisteny.append((slovo.strip(",.:;")).lower())
# print(list_ocisteny)

cviceni = {
    "push_up": {"description": "Push-up exercise", "reps": 15},
    "squat": {"description": "Bodyweight squat", "reps": 20},
    "plank": {"description": "Core strengthening exercise", "duration": "30s"},
    "jumping_jack": {"description": "Full-body cardio exercise", "reps": 25},
    "burpee": {"description": "High-intensity full-body exercise", "reps": 10},
    "lunge": {"description": "Leg strengthening exercise", "reps_per_leg": 10},
    "mountain_climber": {"description": "Core and cardio workout", "duration": "20s"},
    "crunch": {"description": "Abdominal exercise", "reps": 20},
    "deadlift": {"description": "Strength training exercise", "reps": 12},
    "pull_up": {"description": "Upper-body strength exercise", "reps": 8},
    "bicycle_crunch": {"description": "Oblique workout", "reps": 15},
    "high_knees": {"description": "Cardio exercise", "duration": "20s"},
    "leg_raise": {"description": "Abdominal exercise", "reps": 15},
    "tricep_dip": {"description": "Arm and shoulder workout", "reps": 10},
    "side_plank": {"description": "Core and oblique exercise", "duration": "20s"},
    "step_up": {"description": "Leg and glute exercise", "reps_per_leg": 12},
    "skater_jump": {"description": "Plyometric exercise", "reps": 15},
    "bridge": {"description": "Glute and lower back workout", "reps": 20},
    "toe_touch": {"description": "Flexibility and core exercise", "reps": 15},
    "wall_sit": {"description": "Static leg exercise", "duration": "30s"}
}




for k, v in cviceni.items():
    print(k, v)