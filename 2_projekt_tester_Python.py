import time
import random

def vytvor_nah_cislo():
    while True:
        cislo = list(range(10))
        random.shuffle(cislo)
        if cislo[0] != 0:
        
            return "".join(map(str, cislo[:4]))
    

def vstup_uzivatele():
    vstup = input("Zadej číslo o 4 hodnotách: ")
    if len(vstup) != 4 or not vstup.isdigit():
        print("Špatně.")
    else:
        pass
    return vstup

def vyp_bulls(nah_cislo, cislo_uzivatele):
    sum_bulls = sum(1 for n, u in zip(nah_cislo, cislo_uzivatele) if n == u)
    return sum_bulls

def vyp_cows(nah_cislo):
    sum_cows = (sum(1 for uz in cislo_uzivatele if uz in nah_cislo) - bulls)
    return sum_cows


start_cas = int(time.perf_counter())
nah_cislo = vytvor_nah_cislo()
print(nah_cislo)
pocitadlo_smycek = 0

while True:
    pocitadlo_smycek += 1

    cislo_uzivatele = vstup_uzivatele()   
    
    bulls = vyp_bulls(nah_cislo, cislo_uzivatele)
    cows = vyp_cows(nah_cislo)

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
    







