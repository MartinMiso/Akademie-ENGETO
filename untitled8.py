#from decimal import Decimal
print("Mocnináto")
a = int(input("Zadej číslo: "))
b = int(input("Zadej mocninu: "))
result = a
for i in range(b - 1):
    result = result * a
print(f"Výsledek: {result}")
