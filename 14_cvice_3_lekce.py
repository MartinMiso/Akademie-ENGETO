# # cvičení 1 prázdný slovník
# user_1 = {}
# user_1 = {"name" : "Marek", "surname" : "Parek"}
# user_1["name"] = "Marek"
# user_1["surname"] = "Parek"
# user_1.update({"user_email" : "marek.parek@gmail.com"})
# print(f"User #01: ", (user_1))

# #------
# #Řešení ENGETO
# # Zadané proměnné
# user_email = {"email": "marek.parek@gmail.com"}

# # Vytvoř nový slovník "user_1"
# user_1 = dict()

# # Doplň klíče "name" a "surname" s hodnotami "Marek" a "Parek"
# user_1['name'] = 'Marek'
# user_1['surname'] = 'Parek'

# # Doplň slovník "user_1" o slovník "user_email"
# user_1.update(user_email)

# # Vypiš hodnoty ze slovníku "user_1" s doplňujícím textem
# print("User #01:", user_1)

# # ==============================================================


# """ DALŠÍ CVIČENÍ"""
# #cvičení 2 ověření hesla
# uzivatel = {}

# # proměnné
# jmeno = "Marek"
# heslo = "1234"
# uzivatel = {"jmeno" : "Marek", "heslo" : "1234"}

# if uzivatel.get("jmeno") == jmeno and uzivatel.get("heslo") == heslo:
#     print("Ahoj", jmeno, "vítej v aplikaci")

# else:
#     print("Učivatelské jméno nebo heslo nejsou v pořádku")

# #-----
# #řešení ENGETO
# # Uložené přihlašovací údaje
# jmeno = 'Marek'
# heslo = '1234'
# uzivatel = {'Marek': '1234'}

# # Ověř jestli zadané jméno a heslo souhlasí s uloženými údaji ve sl. "uzivatel"
# if uzivatel.get(jmeno) == heslo:
#     # ... pokud SOUHLASÍ, přivítej uživatele jménem
#     print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")

# else:
#     # ... pokud NESOUHLASÍ, upozorni uživatele o omylu
#     print("Uživatelské jméno nebo heslo nejsou v pořádku!")


# # ==============================================================


# """DALŠÍ CVIČENÍ"""
# # 3 cvičení

# cisla_1 = (1, 1, 2, 3, 4)
# cisla_2 = (5, 6, 7, 7, 8)
# set_1 = set(cisla_1)
# set_2 = set(cisla_2)
# #sjednocene_sety = (set_1 | set_2) # nebo funkcní union
# sjednocene_hodnoty = (set_1.union(set_2))
# print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)

# #------

# # Řešení ENGETA
# # Zadané tuply "cisla_1" a "cisla_2"
# cisla_1 = (1, 1, 2, 3, 4)
# cisla_2 = (5, 6, 7, 7, 8)

# # Vytvoř sety a udělej sjednocení jejich hodnot
# # ..do proměnné "sjednocene_hodnoty"
# sjednocene_hodnoty = set(cisla_1) | set(cisla_2)

# # Vypiš uložený výsledek v proměnné "sjednocene_hodnoty"
# print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)

# ==============================================================


"""DALŠÍ CVIČENÍ"""
# 4 cvičení
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}

rozdil_cisel = cisla_1 - cisla_2
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)
# jen blbnutí s for - výpis sloušení
for cislo in cisla_1 | cisla_2:
    print(cislo, end = " ")


#------------------
# Řešení ENGETA
# Zadané tuply "cisla_1" a "cisla_2"
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}

# Vytvoř sety a zjisti jaké ma rozdíly první set oproti druhému
rozdil_cisel = cisla_1.difference(cisla_2)

# Vypiš uložený výsledek v proměnné "nums_1_differences"
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)
