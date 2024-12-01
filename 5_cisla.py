#!/usr/bin/env python3

cisla = []
print("Zadávej čísla a nakonec zadej pouze ENTER pro ukončení zadávání")

# Zde dokonči úlohu svým kódem...

a = int(1)
while a != "":
    print("Zadej číslo: ")
    a = input()
    if a != "":
        a = int(a)
        cisla.append(a)
        
    else:
        break

setridena_cisla = sorted(cisla)
pocet_prvku = len(setridena_cisla)
median = (pocet_prvku//2)
b = (setridena_cisla[median])
for cislo in cisla:
    print(cislo, f"se od mediánu odlišuje o {cislo-b} ")

"""
Dokumentace, co to asi udělá?
"""