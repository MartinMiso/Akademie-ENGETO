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