import random

def vytvor_nah_cislo():
    cislo = list(range(10))
    random.shuffle(cislo)
    return "".join(map(str, cislo[:4]))
    
    
    # cislo = list()
    # for cislice in range(4):
    #     cislice = random.randint(0, 10)
    #     cislo.append(cislice)
    # #print(cislo)
    # return cislo
    
# def vstup_uzivatele():
#     uz_tip = list()
#     uz_tip = list(int(input("Zadej číslo o 4 číslicích: ")))
#     print(uz_tip)
#     return uz_tip
    
    

nah_cislo = vytvor_nah_cislo()
print(nah_cislo)
#hadane_cislo = vstup_uzivatele()


uz_cislo = input("Zadej číslo o 4 hodnotách: ")
if len(uz_cislo) != 4 or not uz_cislo.isdigit():
    print("Špatně.")
   

test = zip(nah_cislo, uz_cislo)

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




