print("Vítejte v kalkulačce")
pokracovat= "ano"
while (pokracovat== "ano"):
    a = float(input("Zadejte první číslo:"))
    b = float(input("Zadejte druhé číslo:"))
    print("Zvolte si operaci:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    volba = int(input())
    vysledek = 0.0
    match volba:
        case 1:
            vysledek = a + b
        case 2:
            vysledek = a - b
        case 3:
            vysledek = a * b
        case 4:
            if b != 0:
                vysledek = a / b
            else:
                print("Nulou nelze dělit!")
                vysledek = "N/A"

    if volba > 0 and volba < 5:
        print(f"Výsledek: {vysledek}")
    else:
        print("Neplatná volba")
    pokracovat = input("Přejete si zadat další příklad? [ano/ne]: ")
print("Děkuji za použití kalkulačky, aplikaci ukončíte libovolnou klávesou.")