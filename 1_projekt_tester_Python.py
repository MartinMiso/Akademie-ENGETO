"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Mišo
email: martin.miso@seznam.cz
"""
TEXTS = ['''Situated about 10 miles west of Kemmerer,
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

import re

# uživatelé
users = {"bob" : "123",
        "ann" : "pass123",
        "mike" : "password123",
        "liz" : "pass123"}
user_register = False
print()

# ověření hesla
name = input("user name: ")#.lower() - případné ověření malých písmen
password = input("your password: ")#.lower()
if users.get(name) == password:
    user_register = True
    print(f"{'-' * 45}")
    print(f"Welcome to the app, {name}")
    print("We have 3 texts to be analyzed.")
    print(f"{'-' * 45}")
    volba = (input("Enter a number btw. 1 and 3 to select: "))
    print(f"{'-' * 45}")

    # proměnné
    cisla = []
    pocet_cisel = 0
    soucet_cisel = 0
    pocet_slov = 0
    velka_pismena = 0
    mala_pismena = 0

    # ANALÝZA TEXTU
    if volba in {"1", "2", "3"}:
        # Výběr textu
        text_index = int(volba) - 1  
        selected_text = TEXTS[text_index]  # Vybraný text
    else:
        print("bad choice, terminating the program..")
        exit()

    delka_textu = len(selected_text.split()) # délka textu

    for cislo in selected_text.split(): # počet čísel a suma čísel
        if cislo.isdigit():
            cisla.append(int(cislo))
            pocet_cisel = len(cisla)
            soucet_cisel = (sum(cisla))
                    
    for zacatek_slov in selected_text.split(): # počet slov začínající velkým písmenem
        if zacatek_slov[0].isupper():
            pocet_slov += 1

    for slovo in selected_text.split(): # počet velkých písmen v textu
        if slovo.isupper() and slovo.isalpha():
            velka_pismena += 1
            
    for mala in selected_text.split(): # počet malých slov v textu
        if mala.islower():
            mala_pismena += 1

    print(f"There are {delka_textu} words in the selected text.") # počet slov
    print(f"Tehere are {pocet_slov} titlecase words.") # počet slov začínající velkými písmeny
    print(f"There are {velka_pismena} uppercase words.") # slova velkými písmeny
    print(f"There are {mala_pismena} lowercase words.") # malá písmena
    print(f"There are {pocet_cisel} numeric string.") # počet čísel
    print(f"The sum of all the numbers {soucet_cisel}") # součet čísel
    
    # četnost délky slov
    ocisteny_text = re.sub(r'[^\w\s]', '', selected_text)
    cetnost = {}
    for slova_textu in ocisteny_text.split():
        delky_slov = (len(slova_textu))
        if delky_slov not in cetnost:
            cetnost[delky_slov] = 0
        cetnost[(delky_slov)] += 1
    serazena_cetnost = dict(sorted(cetnost.items()))
    #print(serazena_cetnost)
        
    # graf
    print(f"{'-' * 45}")
    print("LEN|".rjust(4) + "OCCURENCES".rjust(15) + "|NR.".rjust(11))
    print(f"{'-' * 45}")
    for key, value in serazena_cetnost.items():
        print(f"{key}|".rjust(4), f"{'*' * value}".ljust(20), f"|{value}".ljust(15))
                
else:
    print("unregistered user, terminating the program..")


"""KONEC"""