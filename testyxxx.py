# """VYHOZENÍ PÍSMENA ZE SEZNAMU"""
# """Program odstraní na příní dané písmeno ze seznamu."""

# pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
# print("Začátek", pismena)

# while (len(pismena)) > 0:
    
#     vyhodit = input("Které písmeno chceš vyhodit?")
#     if vyhodit in pismena:
#         pismena.remove(vyhodit)
#         print("Zbývající písmena", pismena)
#     else:
#         print(vyhodit, "není součástí")
# else:
#     print("Seznam je prázdný")


# """CVIČENÍ OD PRVNÍ LEKCE"""

# print(f"Prvních 5 písmen: {"indexování"[:5]}")
# print(f"Posledních 5 písmen: {"indexování"[-5:]}")
# print(f"Každé 3. písmeno (počínaje prvním) od 'i': {"indexování"[::3]}")

# # -------------------------------------- 

# # převodní hodnoty
# kg_lb = 2.20
# km_mile = 0.62
# l_gal = 0.26
# # zadané proměnné - množství
# kg_pocet = 80
# km_pocet = 54
# l_pocet = 5
# # výpočet a výpis
# print(f"{kg_pocet} kg je {kg_pocet*kg_lb} lb")
# print(f"{km_pocet} km je {km_pocet*km_mile} mil")
# print(f"{l_pocet} l je {l_pocet*l_gal}")

# # ------------------------------------------

# mercedes = 150_000
# rolls_royce = 400_000
# vybava = 50_000

# sleva_merc = 5000
# cena_2_merc = (mercedes * 2)
# cena_merc_a_rolls = (mercedes + rolls_royce)
# cena_2_rolls_s_vybavou = (rolls_royce * 2) + (2 * vybava)
# cena_merc_s_vybavou = mercedes + vybava
# merc_se_slevou = mercedes - sleva_merc

# print("Sleva na Mercedes:", sleva_merc)
# print("Cena za dva mercedesy je:", cena_2_merc)
# print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)
# print("Cena za dva Rolse s výbavou:", cena_2_rolls_s_vybavou)
# print("Cena za Mercedes s výbavou:", cena_merc_s_vybavou)
# print("Cena za Mercedes po slevě:", merc_se_slevou)

# ----------------------------------------------------------

# jmeno = "Lukáš"
# prijmeni = "Dvořák"
# cele_jmeno = (jmeno + " " + prijmeni)
# print("Celé jméno:", cele_jmeno)
# delka_jmena = len(cele_jmeno)
# print("Délka jména:", delka_jmena)
# print("=" * delka_jmena)
# print(cele_jmeno)
# print("=" * delka_jmena)

# --------------------------------------------


# zamestnanci = [
#     'František', 'Bruno',
#     'Anna', 'Jakub',
#     'Klára', 'Anežka',
#     'Anežka', 'Anežka'
# ]

# posledni_index = zamestnanci[-1]
# print("Poslední index:", posledni_index)
# print("Na indexu 2 je:", zamestnanci[2])
# print("V intervalu od 2 do 5 je:", zamestnanci[2:6])
# print("Každý třetí člen je:", zamestnanci[::3])

# ---------------------------------------------

# jmeno = "Martin"
# vaha = 80
# vyska = 2

# bmi = (vaha / vyska**2)

# kategorie = ()

# if bmi > 40:
#     kategorie = "těžká obezita"
# elif bmi > 30:
#     kategorie = "obezita"
# elif bmi > 25:
#     kategorie = "mírná nadváha"
# elif bmi > 18.5:
#     kategorie = "zdravá váha"
# else:
#     kategorie = "podvýživa"

# print(jmeno, "tvé BMI je", bmi, "což spadá do kategorie", kategorie,".")

#  -----------------------------------------------------------------------------------

# zamestnanci = ["František", "Anna", "Jakub", "Klára"]
# print("Zaměstnanci na začátku:", zamestnanci)
# zamestnanci_a = zamestnanci.copy()
# zamestnanci_a.append("Bruno, Anežka")
# print("Nová jména přidána:", zamestnanci_a)
# zamestnanci_b = zamestnanci.copy()
# zamestnanci_b.insert(1, "Bruno")
# print("Nová jména vložena:", zamestnanci_b)

#  -------------------------------------------------------------

# vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
# vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
# tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

# cislo_dne = 3

# if cislo_dne in vstupni_cisla:
#     print("Správná vstupní hodnota!")
#     den_tydne = tyden[cislo_dne-1]

#     if den_tydne.startswith(vstupni_pismena[cislo_dne-1]):
#         print("Správné písmeno")
#     else:
#         print("Špatné písmeno")
# else:
#     print("Špatná vstupní hodnota!")

# -----------------------------------------------------------------------------

# user_1 = dict()
# user_1["name"] = "Marek"
# user_1["surname"] = "Parek"
# user_email = {"email" : "marek.parek@gmail.com"}

# user_1.update(user_email)

# print("User #01:",user_1)

# ------------------------------------------------------

# jmeno  ="Marek"
# heslo = "1234"
# uzivatel = {"Marek" : "1234"}

# if uzivatel.get(jmeno) == heslo:
#     print("Ahoj, vítej v aplikaci")
# else:
#     print("Uživatelské jmén nebo heslo jsou špatné")

# -----------------------------------------------------------

# cisla_1 = (1, 1, 2, 3, 4)
# cisla_2 = (5, 6, 7, 7, 8)

# sjednocena_cisla = set(cisla_1) | set(cisla_2)
# print("Sjednocené sety:", sjednocena_cisla)

# --------------------------------------------------

cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
#rozdil_cisel = cisla_1 - cisla_2
rozdil_cisel = cisla_1.difference(cisla_2)
print(rozdil_cisel)