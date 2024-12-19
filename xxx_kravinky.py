

# cislo_1 = float(input())
# cislo_2 = float(input())
# if cislo_1 > cislo_2:
#     print("První číslo je větší než druhé")
# elif cislo_1 == cislo_2:
#     print("Obě čísla jsou stejná")
# else:
#     print("První číslo je menší než druhé")

# test = {"žena", "růže", "píseň", "kost", "kost"}
# print(test)

# cisla = [1, 2, 3, 5, 10]
# soucet = sum(cisla)
# print(soucet)

# import random
# suda_cisla = []
# licha_cisla = []
# cisla = list(range(0, 10000000, 987))
# nahodna_cisla = random.sample(cisla, k=len(cisla))

# for cislo in nahodna_cisla:
#     if cislo % 2 == 0:
#         suda_cisla.append(cislo)
    
#     elif cislo %2 != 0:
#         licha_cisla.append(cislo)

# print("Sudá čísla\n", sorted(suda_cisla))
# print(90 * "-")
# print("Lichá čísla\n", sorted(licha_cisla))



# seznam_slov = words = ['run', 'think', 'jump', 'fly', 'play', 'build', 'talk', 'help', 'read',
#          'speak', 'dance', 'write', 'eat', 'sleep', 'walk', 'fix', 'clean', 'study', 'work',
#          'cook', 'laugh', 'listen', 'travel', 'meet', 'pes', 'watch', 'argue', 'sing', 'hide',
#          'paint', 'jump', 'negotiate', 'learn', 'assist', 'agree', 'disagree', 'invite', 'call',
#          'describe', 'fix', 'organize', 'create', 'close', 'learn', 'laugh', 'prepare', 'teach',
#          'yawn', 'discuss', 'want', 'help', 'drive', 'run', 'eat', 'sleep', 'look', 'find',
#          'understand', 'fix', 'call', 'bake', 'study', 'smile', 'read', 'clean', 'assist', 'play',
#          'organize', 'shout', 'open', 'drop', 'follow', 'disagree', 'argue', 'help', 'complain',
#          'hug', 'write']


# for slovo in seznam_slov:
#     if slovo == "pes":
#         print("Našel jsem psa, přeskakuji cyklus...")
#         break
#     print(slovo)


# import re

# TEXTS = [''' Situated about 10 miles west of Kemmerer,
# Fossil Butte is a ruggedly impressive
# topographic feature that rises sharply
# some 1000 feet above Twin Creek Valley
# to an elevation of more than 7500 feet
# above sea level. The butte is located just
# north of US 30N and the Union Pacific Railroad,
# which traverse the valley. ''',
# '''At the base of Fossil Butte are the bright
# red, purple, yellow and gray beds of the Wasatch
# Formation. Eroded portions of these horizontal
# beds slope gradually upward from the valley floor
# and steepen abruptly. Overlying them and extending
# to the top of the butte are the much steeper
# buff-to-white beds of the Green River Formation,
# which are about 300 feet thick. ''',
# '''The monument contains 8198 acres and protects
# a portion of the largest deposit of freshwater fish
# fossils in the world. The richest fossil fish deposits
# are found in multiple limestone layers, which lie some
# 100 feet below the top of the butte. The fossils
# represent several varieties of perch, as well as
# other freshwater genera and herring similar to those
# in modern oceans. Other fish such as paddlefish,
# garpike and stingray are also present.'''
# ]

# selected_text = TEXTS[0]
# print(selected_text.split())
# cleaned_text = re.sub(r'[^\w\s]', '', selected_text)
# print(cleaned_text)


# cetnost = {}
# for slova_textu in cleaned_text.split():
#     delky_slov = (len(slova_textu))
#     print(delky_slov)
#     if delky_slov not in cetnost:
#         cetnost[delky_slov] = 0
#     cetnost[(delky_slov)] += 1
# serazena_cetnost = dict(sorted(cetnost.items()))
# print(serazena_cetnost)


        
#     # graf
# print(f"{'-' * 45}")
# print("LEN|".rjust(4) + "OCCURENCES".rjust(15) + "|NR.".rjust(11))
# print(f"{'-' * 45}")
# for key, value in serazena_cetnost.items():
#     print(f"{key}|".rjust(4), f"{'*' * value}".ljust(20), f"|{value}".ljust(15))



# VYTVOŘENÍ SLOŽEK V PC
# import os

# jmena_slozek = ("obrazky" , "texty" , "gif")
# slozka = ()

# for slozka in jmena_slozek:
#     if os.path.exists(slozka) and os.path.isdir(slozka):
#         print("Složka existuje")
#     else:
#         os.mkdir(slozka)
#         print(f"Tvořím novou složku: {slozka}")

# print("Všechny složky existují")




#KOSTKY
# import random
# import time

# def hazeni_kostkou():
#     min_hodnota = 1
#     max_hodnota = 6

#     while True:
#         print(f"Házím kostkou ...")
#         time.sleep(1)
#         kostka_hodnota = random.randint(min_hodnota, max_hodnota)
#         print(f"Na kostce je hozena: {kostka_hodnota}")
#         print("-" * len(f"Na kostce je hozena: {kostka_hodnota}"))
#         if kostka_hodnota < 6:
#             print()
#             continue
#         else:
#             break
    

# while True:
#     hazeni_kostkou()
#     pokracovat = input("Chceš pokračovat? Jestli ano, stiskni ,y,")
#     if pokracovat != "y":
#         print("Konec hry")
#         break
