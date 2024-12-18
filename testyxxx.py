pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
print("Začátek", pismena)

while (len(pismena)) > 0:
    
    vyhodit = input("Které písmeno chceš vyhodit?")
    if vyhodit in pismena:
        pismena.remove(vyhodit)
        print("Zbývající písmena", pismena)
    else:
        print(vyhodit, "není součástí")
else:
    print("Seznam je prázdný")

