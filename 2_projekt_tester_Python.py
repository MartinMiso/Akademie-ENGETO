"""
2_projekt_tester_Python.py: druhý projekt do Engeto Online Python Akademie

author: Martin Mišo
email: martin.miso@seznam.cz

"""

import time
import random


def pozdrav():
    """Vrací uvítací pozdrav.
    """
    pozdrav = """Hi there!"""
    return pozdrav


def pravidla_hry():
    """
    Vrací text s pravidly hry.
    """
    text_pravidla = """I've generated a random 4 digit number for you. 
Let's play a bulls and cows game."""
    return text_pravidla


def format_podrtzitka():
    """
    Vytvoří řetězec podtržítek odpovídající délce nejdelšího řádku textu pravidel hry.
    """
    text = pravidla_hry()
    max_delka_radku = max(len(radek) for radek in text.splitlines())
    podtrzitka = ("-" * max_delka_radku)
    return podtrzitka


def vytvor_nah_cislo():
    """
    Vrací čtyřciferné náhodné číslo jako řetězec, první číslice nesmí být nula.

    Funkce provádí následující kroky:
    1. Vytvoří seznam číslic 0-9.
    2. Náhodně promíchá pořadí číslic v seznamu.
    3. Zkontroluje, zda první číslice není 0.
    4. Pokud podmínka splněna, spojí prvních 4 číslice do řetězce a vrátí je.
       Pokud podmínka není splněna, opakuje proces.
    """
    while True:
        cislo = list(range(10))
        random.shuffle(cislo)
        if cislo[0] != 0:
        
            return "".join(map(str, cislo[:4]))
    

def vstup_uzivatele():
    """
    Vrací 4 ciferné číslo, které splňuje zadané podmínky.

    Funkce opakovaně požaduje vstup od uživatele, dokud nezadá správné číslo. 
    Číslo musí splňovat následující podmínky:
    1. Obsahuje přesně 4 číslice.
    2. Neobsahuje žádné duplicitní číslice.
    3. Obsahuje pouze číslice (žádné jiné znaky).

    Pokud uživatel zadá neplatné číslo, funkce zobrazí chybovou zprávu a požaduje nový vstup.
    """
    while True:
        vstup = input(">>> ")
        str_cislo = str(vstup)
        mnozina_cisel = set(str_cislo)
        if len(vstup) != 4 or not vstup.isdigit() or len(vstup) != len(mnozina_cisel):
            print("Číslo musí obsahovat pouze číslice, mít jen 4 znaky a žádné duplicity. Zadej číslo znova.")
        else:
            return vstup


def vyp_bulls(nah_cislo, cislo_uzivatele):
    """
    Vrací počet stejných číslic na správné pozici mezi dvěma čísly.

    Funkce porovnává dvě čísla a počítá, kolik číslic má 
    uživatelovo číslo na správných pozicích.

    Parametry:
        nah_cislo (str): Náhodně generované číslo jako řetězec.
        cislo_uzivatele (str): číslo zadané uživatelem jako řetězec.
        n: reprezentuje náhodné číslo
        u: reprezentuje uživatelské číslo
    """
    sum_bulls = sum(1 for n, u in zip(nah_cislo, cislo_uzivatele) if n == u)
    return sum_bulls


def vyp_cows(nah_cislo, cislo_uzivatele, bulls):
    """
    Vrací počet stejných číslic na správné pozici mezi dvěma čísly.

    Funkce porovnává dvě čísla a počítá, kolik číslic má 
    uživatelovo číslo na správných pozicích.
    Následně se z celkového počtu shodných číslic odečte počet "bulls".

    Parametry:
        nah_cislo (str): Náhodně generované číslo jako řetězec.
        Proměnná `bulls` musí být předána nebo definována mimo tuto funkci.
        uz: reprezentuje uživatelské číslo
    """
    sum_cows = (sum(1 for uz in cislo_uzivatele if uz in nah_cislo) - bulls)
    return sum_cows


def main():
    """
    Spustí hlavní logiku hry Bulls and Cows.

    Provádí následující kroky:
    1. Vypíše uvítací pozdrav a pravidla hry.
    2. Vygeneruje náhodné číslo podle podmínek.
    3. Spustí herní smyčku, která porovnává vstup uživatele s náhodným číslem.
    4. Po uhodnutí čísla vypíše statistiky (počet pokusů a čas hry).
    """

    # výpis uvítacího pozdravu a pravidel hry
    print(pozdrav())
    print(format_podrtzitka())
    print(pravidla_hry())
    print(format_podrtzitka())

    # Počátek počítání času ve vteřinách od spuštění hry
    start_cas = int(time.perf_counter())

    # Inicializace funkce náhodného čísla
    nah_cislo = vytvor_nah_cislo()
    #print(nah_cislo)

    pocitadlo_smycek = 0 # nastavení počítadla smyček na nulu

    while True:
        pocitadlo_smycek += 1 # přičtení čísla při každém průběhu smyčky

        # přírazení a volání funkcí pro průběh hry
        cislo_uzivatele = vstup_uzivatele()   
        
        bulls = vyp_bulls(nah_cislo, cislo_uzivatele)
        cows = vyp_cows(nah_cislo, cislo_uzivatele, bulls)

        # logika výpisu BULL/BULLS, COW/COWS
        if bulls != 4:
            bull = "BULL" if bulls == 1 else "BULLS"
            cow = "COW" if cows == 1 else "COWS"
                        
            print(f"{bulls} {bull}, {cows} {cow}")
            print(format_podrtzitka())

        # výpis o uhádnutí čísla a ukončení hry
        else:
            end_cas = int(time.perf_counter()) # konec počítání času hry
            print(f"Correct, you've guessed the right number \n"
                f"in 4 guesses! \n"
                f"Number of attempts: {pocitadlo_smycek}\n"
                f"Length of the game: {end_cas - start_cas} seconds")
            print(format_podrtzitka())
            print("That's amazing!")

            break

if __name__ == "__main__":
    main()

# konec






