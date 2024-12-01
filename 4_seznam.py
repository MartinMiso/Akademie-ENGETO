#!/usr/bin/env python3

zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev", "mrkev", "brokolice"]
ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]

# Zde dokonči úlohu svým kódem...
seznam1 = []
pokracovat = "ano"
while (pokracovat=="ano"):
    druh = input("Zadej název libovolného ovoce nebo zeleniny: ")
    seznam1.append(druh)
    if druh in zelenina:
        pozice = zelenina.index(druh);
        print("Zadal jsi zeleninu")
    elif druh in ovoce:
        pozice2 = ovoce.index(druh);
        print("Zadal jsi ovoce")
    else:
        print("Tvoje slovo nemám v seznamu")
    pokracovat = input("Přeješ si zadat další slovo? (ano/ne) ")
pocet = len(seznam1)
print(f"Zadal jsi {pocet} slov")

