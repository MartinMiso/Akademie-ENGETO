#!/usr/bin/env python3

zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev", "mrkev", "brokolice"]
ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]

# Zde dokonči úlohu svým kódem...


pokracovat= "ano"
while (pokracovat== "ano"):
    druh = input("Zadej název libovolného ovoce nebo zeleniny: ")
    if druh in (zelenina):
        pozice1 = zelenina.index(druh);
        print("Zadal jsi zeleninu")
    elif druh in (ovoce):
        pozice2 = ovoce.index(druh);
        print("Zadal jsi ovoce")
    else:
        print("Nemám v seznamu")
    pokracovat = input("Chceš zadat další příklad? [ano/ne]: ")
    pocet = []
    pocet.extend(pokracovat)
print(pocet)
print("Díky")
    
    
    