

# cislo_1 = float(input())
# cislo_2 = float(input())
# if cislo_1 > cislo_2:
#     print("První číslo je větší než druhé")
# elif cislo_1 == cislo_2:
#     print("Obě čísla jsou stejná")
# else:
#     print("První číslo je menší než druhé")

# test = {"žena", "růže", "píseň", "kost", "kost"}
# print(test)

# cisla = [1, 2, 3, 5, 10]
# soucet = sum(cisla)
# print(soucet)

import random
suda_cisla = []
licha_cisla = []
cisla = list(range(0, 100))
nahodna_cisla = random.sample(cisla, k=len(cisla))

for cislo in nahodna_cisla:
    if cislo % 2 == 0:
        suda_cisla.append(cislo)
    
    elif cislo %2 != 0:
        licha_cisla.append(cislo)

print("Sudá čísla\n", sorted(suda_cisla))
print(90 * "-")
print("Lichá čísla\n", sorted(licha_cisla))

        

