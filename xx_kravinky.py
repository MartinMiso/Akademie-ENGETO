cislo = int(input("Číslo: "))
vysledek = None

if ((cislo % 3) == 0 and (cislo % 5) == 0):
    vysledek = "FizzBuzz"
elif ((cislo % 3) == 0):
    vysledek = "Fizz"
elif ((cislo % 5) == 0):
    vysledek = "Buzz"
else:
    vysledek = cislo

print(vysledek)