text = """
koupelna
zona
syr
teta
kriz
rodina
nacitani
cokolada
asociace
lavicka
povrch
rotace
zamestnanec
balicek
komunikace
popularni
veta
"""
# with open ("slova.txt", "w", encoding = "UTF-8") as txt_soubor:
#     txt_soubor.write(text)
#     print("Text zapsán")

# def zobraz_slova(textovy_soubor):
#     with open(textovy_soubor, "r", encoding="UTF-8") as txt_soubor:
#         radky = txt_soubor.read()
#         slova = radky.split()
#         for slovo in slova:
#             if len(slovo) >= 7:
#                 print(slovo)
        
# zobraz_slova("slova.txt")

# Otevri textovy soubor v modu cteni
# def zobraz_slova(textovy_soubor):
#     """
#     Vytvor funkci, ktera otevre textovy soubor a precte slova.
#     """
#     zadana_slova = open(textovy_soubor, "r")

#     data = zadana_slova.read()
#     slova = data.split()

#     for slovo in slova:
#         if len(slovo) >= 7:
#             print(slovo, end=" ")
#     zadana_slova.close()

# prvni_radek = "První řádek v souboru,\n"
# druhy_radek = "druhý řádek v souboru,\n"
# treti_radek = "třetí řádek v souboru."

# with open ("txt_soubor.txt", "w", encoding="UTF-8") as txt_soubor:
#     txt_soubor.writelines([prvni_radek, druhy_radek, treti_radek])
#     # txt_soubor.write(prvni_radek)
#     # txt_soubor.write(druhy_radek)
#     # txt_soubor.write(treti_radek)
    
# with open("txt_soubor.txt", "r", encoding="UTF-8") as txt_soubor:    
#     cteni_txt = txt_soubor.read()
#     obsah_txt = cteni_txt
#     print(obsah_txt)

# kombinace = 1.234
# presnost_str = "Hello"
# presnost_cisla = 123.4567

# formatovana_presnost = (f"|{presnost_cisla:.2e}|{presnost_cisla:.1f}|{presnost_cisla:.2f}|")
# print(formatovana_presnost)

# formatovaci_kombinace = (f"|{kombinace:.3f}$|")
# print(formatovaci_kombinace)

# formatovaci_presnost_str = (f"|{presnost_str:.4}|")
# print(formatovaci_presnost_str)

# text = """
# Python,
# Scala,
# JavaScript,
# Java.
# """
# def nacti_radky(cesta_k_souboru: str):
#     try:
#         soubor = open(cesta_k_souboru)

#     except FileNotFoundError:
#         print(f'Soubor: {cesta_k_souboru} neexistuje!')
#         obsah = []
#     else:
#         obsah = soubor.read()
#         soubor.close()
#     finally:
#         return obsah


# vysledek = nacti_radky("jazyky.txt")
# print(vysledek)


# def nacti_radky(cesta_k_souboru: str):
#     try:
#         soubor = open(cesta_k_souboru)

#     except FileNotFoundError:
#         vstup = input(f"Soubor: {cesta_k_souboru} neexistuje. Chcete soubor vytvořit? A/N: ")
#         if vstup == "A":
#             with open ("jazyky.txt", "w", encoding="UTF-8") as file:
#                 file.write(text)
#         else:
#             print("Soubor nenalezen ani nezapsán")
#         obsah = []
    
#     else:
#         obsah = soubor.read()
#         soubor.close()
    
#     finally:
#         return obsah

# vysledek = nacti_radky("jazyky.txt")
# print(vysledek)
    


# def secti_hodnoty(udaje):
#     vysledek = 0.0
#     for hodnota in udaje:
#         try:
#             cisla = float(hodnota)
    
#         except Exception:
#             print(f"Hodnota {hodnota} není číselný údaj.")

#         else:
#             vysledek += float(cisla)
    
#     return vysledek

# test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\\n', 4]
# print(f"Výsledek {secti_hodnoty(test)}")

# muj_slovnik = {
#     'jmeno':'Pepa',
#     'prijmeni': 'Novak',
#     'rok_narozeni': 1990
# }

# def obsahuje_klic_a_hodnotu(klic: str, hodnota: str, slovnik: dict):
#     try:
#         nalezena_hodnota = slovnik[klic]
#     except KeyError:
#         print(f"Klíč {klic} nenalezen.")
#         vysledek = False

#     else:
#         print(f"Klíč {klic} nalezen.")

#         if nalezena_hodnota == hodnota:
#             vysledek = True
#         else:
#             print(f"Hodnota {hodnota} nenalezena.")
#             vysledek = False
#     finally:
#         return vysledek

# print(obsahuje_klic_a_hodnotu("jmeno", "Pepa", muj_slovnik))

# import csv
# from typing import List, Dict, Any  # Volitelné

# def zpracuj_vsechny_uzivatele(data, cesta_k_souboru):
#     with open(cesta_k_souboru, "w", encoding="utf-8") as csv_soubor:
#         zapisovac = csv.DictWriter(csv_soubor, fieldnames=data[0].keys())
    

# def filtruj_nezadouci_sloupce(zadany_slovnik, nezadouci):
#     vysledny_slovnik = {}
        
#         for klic, hodnota in zadany_slovnik.items():
#             if klic in nezadouci:
#                 continue
#             vysledny_slovnik[klic] = hodnota
#         return vysledny_slovnik

# def zpracuj_vsechny_uzivatele(zadane_hodnoty, nezadouci):
#     vysledny_list_slovniku = [
#         filtruj_nezadouci_sloupce(sloupce, nezadouci)
#         for slovnik in zadane_hodnoty
#     ]

#     return tuple(vysledny_list_slovniku)

# def zapis_jako_csv_soubor(data, cesta_k_souboru):
#     with open(cesta_k_souboru, "w", encoding="utf-8") as csc_soubor:
#         zapisovac = csv.DictWriter(csv_soubor, fieldnames=data[0].keys())





# data = [  # namedtuple
#     {"name": "Alice", "age": 23, "score": 85},
#     {"name": "Bob", "age": 27, "score": 90},
#     {"name": "Charlie", "age": 22, "score": 87},
#     {"name": "Diana", "age": 24, "score": 92},
#     {"name": "Edward", "age": 29, "score": 88}
# ]
import os
import json
import sys
import csv
import argparse
from files_dir import Path


parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--files_dir", type=str, default="data", help="Cesta ke složce s json soubory"
)

# Najít vsechny json soubory
# Pro kazdy json - nacist, filtrace, zapsat do csv

def find_all_json_files(files_dir: str | Path):
    all_json_fpaths = []
    for fname in os.listdir(files_dir):
        #fname.split(".")[-1] == "json"
        if fname.endswith(".json"):
            all_json_fpaths.append(os.path.join(files_dir, fname))
    return all_json_fpaths


def read_json(json_fpath: str) -> dict:
    with open(json_fpath, "r", encoding="utf-8") as f:
        return json.load(f)
    
def filter_keys(contents: dict, keys_to_save=("jmeno", "konkurence")) -> dict:
    filtered_contents = {}
    for key, value in contents.items():
        if key in keys_to_save:
    return keys_to_save
    

def write_to_csv(csv_fpath: str, contenst: dict):
    with open(csv_fpath, "w", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=contenst[0].keys())
        csv_writer.writeheader()
        csv_writer.writerow(contenst)


def main():
    files_dir = sys.argv[1]
    print()
    find_all_json_files(files_dir)
    for json_fpath in find_all_json_files:
        contenst = read_json(json_fpath)
    # filter
        write_to_csv("test.csv", filtered_contenst)

    print(sys.argv)

if __name__ == "__main__":
    main()
