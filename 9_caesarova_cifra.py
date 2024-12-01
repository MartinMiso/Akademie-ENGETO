retezec = input("Zadej větu k šifrování: ")
posun = int(input("Zadej o kolik bude posun: "))
print("Původní zrpáva:", retezec)
zprava = ""


# cyklus projíždějící znaky
for znak in retezec:
    i = ord(znak)
    i = i + posun
    # kontrola přetečení
    if (i > ord("z")):
        i = i - 26
    znak = chr(i)
    zprava = zprava + znak
# výpis
print("Zašifrovaná zpráv:", zprava)
input()


# cyklus dešifrování
for znak in zprava:
    i = ord(znak)
    i = i - posun
    # kontrola přetečení
   #if (i > ord("z")):
    #    i = i + 26
    znak = chr(i)
    zprava = zprava + znak
print("Dešiffrovaná věta:", zprava)