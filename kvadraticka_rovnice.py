print("Program na výpočet kvadratické rovnice")
print("Tvar rovnice: ax^2+bx+c=0")
a = float(input("Zadej koeficient a: "))
b = float(input("Zadej koeficient b: "))
c = float(input("Zadej koeficient c: "))
if a != 0:
    d = b*b - 4*a*c
    if d < 0:
        print("Rovnice nemá řešení v oboru reálných čísel")
    elif d == 0:
        x = -b/(2*a)
        print("Rovnice má jeden kořen: ")
        print(x)
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print("Rovnice má dva kořeny: ")
        print(x1)
        print(x2)
else:
    print("Není kvadratická rovnice")
input()