# zadání vstupu
print("Zadejte text k zašifrování: ")
vstup = input()
print("Zadejte heslo: ")
heslo = input()
vystup = ""
# průchod všemi znaky ve vstupu
for i, znak in enumerate(vstup):
    # výpočet posunu v abecedě
    x = ord(heslo[i % len(heslo)]) - (ord("a") - 1)
    # ošetření přeteční přes z
    if ord(znak) + x > ord("z"):
        x -= ord("z") - ord("a") + 1
    # získání transformovaného znaku
    vysledek = chr(ord(znak) + x)
    # přidání znaku do výstupu
    vystup += vysledek
print("Výsledek:", vystup)
input()
