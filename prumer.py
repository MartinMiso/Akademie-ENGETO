#!/usr/bin/env python3

print("Výpočet průměru známek")
print("Zadejte známky oddělené čárkou: ")

vstup = input()

# Zde dokonči úlohu svým kódem...
cisla = list(map(int, vstup.split(",")))
soucet = (sum(cisla)) / (len(cisla))

print(f"Průměr: {float(soucet)}")

print(dir(map))