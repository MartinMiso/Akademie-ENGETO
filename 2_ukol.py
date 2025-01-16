import random

def vytvor_nah_cislo():
    while True:
        cislo = list(range(10))
        random.shuffle(cislo)
        if cislo[0] != 0:
        
            return "".join(map(str, cislo[:4]))
    

nah_cislo = vytvor_nah_cislo()
print(nah_cislo)
#hadane_cislo = vstup_uzivatele()


uz_cislo = input("Zadej číslo o 4 hodnotách: ")
if len(uz_cislo) != 4 or not uz_cislo.isdigit():
    print("Špatně.")
else:
    pass
   
test = zip(nah_cislo, uz_cislo)

bulls = sum(1 for n, u in test if n == u)
for n, u in test:
    if n == u:
        print("Máš býka")
    else:
        pass#print("Neuhádl jsi číslo")
for uz in uz_cislo:
    if uz in nah_cislo:
        print("Máš krávu")
    else:
        pass#print("Neuhádl jsi číslo")
print(f"Nahodné číslo: {nah_cislo}, Uživatelské číslo: {uz_cislo}")




