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

users = {"bob" : "123",
        "ann" : "pass123",
        "mike" : "password123",
        "liz" : "pass123"}

user_register = False

# password verify

name = input("User name: ")#.lower() - případné ověření malých písmen
password = input("Your password: ")#.lower()
if users.get(name) == password:
    user_register = True
    print()
    print(f"{'-' * 40}")
    print(f"Welcome to the app {name}")
    print("We have 3 texts to be analyzed.")
    print(f"{'-' * 40}")
    volba = (input("Enter a number btw. 1 and 3 to select: "))
    print(f"{'-' * 50}")

    cisla = []
    pocet_cisel = 0
    soucet_cisel = 0
    pocet_slov = 0
    velka_pismena = 0
    mala_pismena = 0

    if volba in {"1", "2", "3"}:
        # Vybere text podle čísla (volba 1 -> text_1, volba 2 -> text_2 atd.)
        text_index = int(volba) - 1  # Volba 1 bude index 0, volba 2 bude index 1 atd.
        selected_text = TEXTS[text_index]  # Vybraný text 

    long_text = len(selected_text.split()) # délka textu

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
            
    for mala in selected_text.split(): # počet velkýchmalých slov v textu
        if mala.islower():
            mala_pismena += 1

    print("Počet slov", long_text) # počet slov
    print("Slova začínající velkými písmeny", pocet_slov) # počet slov začínající velkými písmeny
    print("Počet slov psaný velkými písmeny", velka_pismena) # velká písmena
    print("Počet slov s malý písmen", mala_pismena) # počet čísel
    print("Počet čísel", pocet_cisel)
    print("Součet čísel", soucet_cisel) # součet čísel
    print()

    cetnost = {}
    for slova_v_textu in selected_text.split():
        delky_slov = (len(slova_v_textu))
        if delky_slov not in cetnost:
            cetnost[delky_slov] = 0
        cetnost[(delky_slov)] += 1
    serazena_cetnost = dict(sorted(cetnost.items()))
        #print(serazena_cetnost)
        
    # formát řádkování
    #graf
    print(f"{'-' * 50}")
    print("LEN|".rjust(4) + "OCCURENCES".rjust(13) + "|NR.".rjust(8))
    print(f"{'-' * 40}")
    for key, value in serazena_cetnost.items():
        print(f"{key}|".rjust(4), f"{'*' * value}".ljust(15), f"|{value}".ljust(10))
                
else:
    print("Sorry, you must go out!")
        


# # if user_register:
# #     chose_text == True
# #     print("Jsi registrovaný")
# #     print()
# #     text_analyze()

#     # if chose_text == True:
#     #     
        
#     #     for cislo in (text_1.split()): # počet čísel a suma čísel
#     #          if cislo.isdigit():
#     #             cisla.append(int(cislo))
#     #             pocet_cisel = len(cisla)
#     #             soucet_cisel = (sum(cisla))
                
#     #     for zacatek_slov in (text_1.split()): # počet slov začínající velkým písmenem
#     #         if zacatek_slov[0].isupper():
#     #             pocet_slov += 1

#     #     for znak in (text_1.split()): # počet velkých písmen v textu
#     #         if znak.isupper():
#     #             velka_pismena += 1
        
#     #     for mala in (text_1.split()): # počet velkýchmalých slov v textu
#     #         if mala.islower():
#     #             mala_pismena += 1

#     # print("Počet slov", long_text) # počet slov
#     # print("Slova začínající velkými písmeny", pocet_slov) # počet slov začínající velkými písmeny
#     # print("Velká písmena", velka_pismena) # velká písmena
#     # print("Počet malých písmen", mala_pismena) # počet čísel
#     # print("5Počet čísel", pocet_cisel)
#     # print("Součet čísel", soucet_cisel) # součet čísel

# # graf
# print()
# seznam_text = []
# seznam_text.append(text)
# #print(seznam_text)
# print()
# cetnost = {}
# for slova_v_textu in text_1.split():
#     delky_slov = (len(slova_v_textu))
#     if delky_slov not in cetnost:
#         cetnost[delky_slov] = 0
#     cetnost[(delky_slov)] += 1
# serazena_cetnost = dict(sorted(cetnost.items()))
# #print(serazena_cetnost)
# # formát řádkování
# print("LEN|".rjust(4) + "OCCURENCES".rjust(13) + "|NR.".rjust(8))
# print(f"{'-' * 40}")
# for key, value in serazena_cetnost.items():
#     print(f"{key}|".rjust(4), f"{'*' * value}".ljust(15), f"|{value}".ljust(10))