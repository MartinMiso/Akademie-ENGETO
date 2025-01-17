"""
2_projekt_tester_Python.py: druhý projekt do Engeto Online Python Akademie

author: Martin Mišo
email: martin.miso@seznam.cz
"""

import time
import random

def vytvor_nah_cislo():
    while True:
        nah_cislo = list(range(10))
        random.shuffle(nah_cislo)
        if nah_cislo[0] != 0:
        
            return "".join(map(str, nah_cislo[:4]))
    

def vstup_uzivatele():
    vstup = input("Zadej číslo o 4 hodnotách: ")
    return True

def overeni_duplicity(vstup):
    cislo = str(vstup)
    mnozina_cisel = set(cislo)

    if len(mnozina_cisel) != len(cislo):
        return True # číslo obsahuje duplicity
    return False # číslo neobsahuje duplicity

def overeni_znaky(cislo):
    if len(cislo) != 4 or not cislo.isdigit():
        return True # číslo neobsahuje pouze číslice nebo není na 4 znaky
    return False # číslo je v pořádku

def vyp_bulls(nah_cislo, cislo_uzivatele):
    sum_bulls = sum(1 for n, u in zip(nah_cislo, cislo_uzivatele) if n == u)
    return sum_bulls

def vyp_cows(nah_cislo):
    sum_cows = (sum(1 for uz in cislo_uzivatele if uz in nah_cislo) - bulls)
    return sum_cows



start_cas = int(time.perf_counter())
nahodne_cislo = vytvor_nah_cislo()
print(nahodne_cislo)
pocitadlo_smycek = 0

while True:
    pocitadlo_smycek += 1

    cislo_uzivatele = vstup_uzivatele()
    if overeni_duplicity(cislo_uzivatele):
        print("Číslo nesmí obsahovat duplicity - zadej nové číslo.")
        continue

    if overeni_znaky(cislo_uzivatele):
        print("Musí obsahovat pouze čísla.")
        continue
    
    bulls = vyp_bulls(nahodne_cislo, cislo_uzivatele)
    cows = vyp_cows(nahodne_cislo)

    if bulls != 4:        
        if bulls == 1:
            bull = "BULL"
        else:
            bull = "BULLS"
        if cows == 1:
            cow = "COW"
        else:
            cow = "COWS"        
        print("Hádej znova")
        print(f"Máš {bulls} {bull} a {cows} {cow}.")

    else:
        end_cas = int(time.perf_counter())
        print(f"Výborně, uhádl jsi na {pocitadlo_smycek}. pokus a trvalo ti to {end_cas - start_cas} sekund!")
        
        break
    







