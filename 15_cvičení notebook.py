# """ CVIČENÍ LEKCE 2 """

# # Ze stringu "matous.holinka@gmail.com", získej jenom "matous.holinka",
# # nahraď ve "matous.holinka" znak "." pomocí mezery " ",
# # vypiš jméno title-case, tedy "Matous Holinka".

# jmeno = "matous.holinka@gmail.com".split("@")
# #print(jmeno[0])
# matous = jmeno[0]
# #print(matous)

# holinka = "matous.holinka".replace(".", " ")
# #print(holinka)
# print(holinka.title())

# # ----------------------------------------
# # ŘEŠENÍ ENGETA
# print("matous.holinka@gmail.com".split("@")[0].replace(".", " ").title())


# """ KRAVINKY A ZKOUŠENÍ ---------------------------------------"""

# jmena = ["Martin Mišo", "Jana Kunovská", "Jirka Vávra", "Tadeáš Řehák", "Honza Plánička"]
# print(jmena)
# for jmeno in jmena:
#     rozdelena_jmena = jmeno.split(",")
#     print(rozdelena_jmena)

# CVIČENÍ 2

# data = ['2021-01-01 11:11:11:1111 - něco se děje,',
# '2021-01-01 11:12:11:1111 - nic to nebylo,',
# '2021-01-01 11:13:11:1111 - a přece něco!,']


# for udaje in data:
#     rozdelena_data = udaje.split(",")[0]
#     print(rozdelena_data)

# print()

# data.insert(0, "2021-01-01 11:10:11:1111 - BANG,\n")
# print(data)
# print()
# #data.insert(4, "2021-01-01 11:14:11:1111 - BANG BANG!,\n")
# data.append("2021-01-01 11:14:11:1111 - BANG BANG!,\n")
# print(data)


"""DOMÁCÍ ÚKOL - HESLO"""
# Vytvoř takový podmínkový zápis, který bude reagovat na nesprávně zadaná hesla (viz. příklad níže):
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

while True:
    heslo = input("Zadej heslo: ")

    if heslo == "":
        print("Vynechal jsi pole s heslem!")
    elif heslo[0].isdigit():
        print("Heslo nesmí začínat číselným znakem")
    elif not (any(char.isdigit() for char in heslo) and any(char.isalpha() for char in heslo)):
        print("Heslo musí obsahovat jak číselné znaky, tak písmena")
    elif len(heslo) < 8:
        print("Heslo musí být alespoň 8 znaků dlouhé")
    elif "@" in heslo:
        print("Heslo nesmí obsahovat '@'")
    else:
        print("Heslo je v pořádku")
        break

# -------------------------------
# ŘEŠENÍ ENGETO

# heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
# heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
# heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
# heslo_3 = "12345678"    # FAIL -> "Heslo nesmí začínat číselným znakem"
# heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
# heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
# heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

# heslo = heslo_3

# if not heslo:
#     print("Vynechal jsi pole s heslem!")
# elif heslo[0].isdigit() and not heslo.isnumeric():
#     print("Heslo nesmí začínat číselným znakem")
# elif len(heslo) < 8:
#     print("Heslo musí být alespoň 8 znaků dlouhé")
# elif heslo.find("@") != -1:
#     print('Heslo nesmí obsahovat \"@\"')
# elif heslo.isnumeric() or heslo.isalpha():
#     print("Heslo musí obsahovat jak číselné znaky, tak písmena")
# else:
#     print("Heslo je v pořádku")


