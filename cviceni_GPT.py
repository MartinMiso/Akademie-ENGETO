"""
## 10 Reálnější cvičení na programování v Pythonu

---

### **1. Kalkulačka (Základy výpočtů)**
**Úkol:**  
Vytvořte program, který funguje jako jednoduchá kalkulačka. Uživateli umožní zadat dvě čísla a vybrat matematickou operaci (+, -, *, /). Program provede požadovaný výpočet a zobrazí výsledek.  

**Postup:**  
1. Požádejte uživatele o zadání dvou čísel.  
2. Zeptejte se na typ operace, kterou chce provést.  
3. Použijte podmínky (if/elif) k provedení výpočtu.  
4. Ošetřete chybu při dělení nulou.  
5. Zobrazte výsledek nebo chybovou zprávu.  

**Řešení:**  
```python
cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
operace = input("Zadej operaci (+, -, *, /): ")

if operace == '+':
    vysledek = cislo1 + cislo2
elif operace == '-':
    vysledek = cislo1 - cislo2
elif operace == '*':
    vysledek = cislo1 * cislo2
elif operace == '/':
    if cislo2 != 0:
        vysledek = cislo1 / cislo2
    else:
        vysledek = "Dělení nulou není povoleno."
else:
    vysledek = "Neplatná operace."

print(f"Výsledek: {vysledek}")
```

---

### **2. Správa kontaktů (Práce se slovníky)**
**Úkol:**  
Vytvořte program pro správu kontaktů. Program umožní uživateli přidat nový kontakt, odebrat existující kontakt a zobrazit všechny kontakty.  

**Postup:**  
1. Použijte slovník pro uložení jmen a telefonních čísel.  
2. Vytvořte cyklus, který umožní opakované zadávání příkazů.  
3. Implementujte možnosti pro přidání, odstranění a zobrazení kontaktů.  
4. Ošetřete chyby, například neexistující kontakt.  

**Řešení:**  
```python
kontakty = {}

while True:
    print("\nMožnosti: \n1 - Přidat kontakt\n2 - Odebrat kontakt\n3 - Zobrazit kontakty\n4 - Konec")
    volba = input("Vyber možnost: ")

    if volba == '1':
        jmeno = input("Zadej jméno: ")
        cislo = input("Zadej číslo: ")
        kontakty[jmeno] = cislo
        print("Kontakt přidán.")
    elif volba == '2':
        jmeno = input("Zadej jméno ke smazání: ")
        if jmeno in kontakty:
            del kontakty[jmeno]
            print("Kontakt odstraněn.")
        else:
            print("Kontakt nenalezen.")
    elif volba == '3':
        for jmeno, cislo in kontakty.items():
            print(f"{jmeno}: {cislo}")
    elif volba == '4':
        break
    else:
        print("Neplatná volba.")
```

---

### **3. Analýza textu (Počet slov a písmen)**
**Úkol:**  
Napište program, který analyzuje text zadaný uživatelem. Program spočítá počet slov a zjistí výskyt jednotlivých písmen.  

**Postup:**  
1. Požádejte uživatele o zadání textu.  
2. Rozdělte text na slova a spočítejte jejich počet.  
3. Projděte jednotlivé znaky textu a spočítejte jejich četnost (použijte slovník).  
4. Výsledky zobrazte uspořádané podle abecedy.  

**Řešení:**  
```python
text = input("Zadej text: ").lower()
pocet_slov = len(text.split())
statistika = {}

for znak in text:
    if znak.isalpha():
        statistika[znak] = statistika.get(znak, 0) + 1

print(f"Počet slov: {pocet_slov}")
print("Výskyt písmen:")
for pismeno, pocet in sorted(statistika.items()):
    print(f"{pismeno}: {pocet}")
```

---

### **4. Generátor náhodných hesel**
**Úkol:**  
Vytvořte program, který vygeneruje náhodné heslo o zadané délce. Heslo bude obsahovat malá i velká písmena, čísla a speciální znaky.  

**Postup:**  
1. Požádejte uživatele o zadání délky hesla.  
2. Použijte knihovnu `random` k výběru náhodných znaků.  
3. Kombinujte různé typy znaků z knihovny `string`.  
4. Vygenerované heslo zobrazte.  

**Řešení:**  
```python
import random
import string

delka = int(input("Zadej délku hesla: "))
heslo = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=delka))
print(f"Generované heslo: {heslo}")
```

---

### **5. Fibonacciho posloupnost (Rekurze)**
**Úkol:**  
Napište program, který vypočítá n-tý člen Fibonacciho posloupnosti. Fibonacciho posloupnost začíná čísly 0 a 1, přičemž každé další číslo je součtem dvou předchozích.  

**Postup:**  
1. Vytvořte rekurzivní funkci pro výpočet n-tého členu.  
2. Ověřte, že vstup je platné číslo.  
3. Zobrazte výsledek výpočtu.  

**Řešení:**  
```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Zadej pořadí členu: "))
print(f"{n}. člen Fibonacciho posloupnosti je {fibonacci(n)}")
```

---
## Pokročilá cvičení na programování v Pythonu (6–10)

---

### **6. Kontrola platnosti hesla**
**Úkol:**  
Vytvořte program, který zkontroluje, zda zadané heslo splňuje požadavky na bezpečnost. Heslo musí:
- Mít alespoň 8 znaků.
- Obsahovat alespoň jedno velké písmeno, jedno malé písmeno, jedno číslo a jeden speciální znak.

**Postup:**  
1. Požádejte uživatele o zadání hesla.  
2. Použijte regulární výrazy nebo podmínky k ověření požadavků.  
3. Zobrazte výsledek kontroly.  

**Řešení:**  
```python
import re

heslo = input("Zadej heslo: ")

if (len(heslo) >= 8 and
    re.search(r'[A-Z]', heslo) and
    re.search(r'[a-z]', heslo) and
    re.search(r'[0-9]', heslo) and
    re.search(r'[!@#$%^&*(),.?":{}|<>]', heslo)):
    print("Heslo je platné.")
else:
    print("Heslo nesplňuje požadavky.")
```

---

### **7. Automatická kontrola palindromu**
**Úkol:**  
Napište program, který zjistí, zda je zadaný text palindrom (čte se stejně zleva i zprava). Program ignoruje mezery a rozdíly mezi malými a velkými písmeny.  

**Postup:**  
1. Požádejte uživatele o zadání textu.  
2. Odstraňte mezery a převeďte text na malá písmena.  
3. Zkontrolujte, zda je text shodný sám se sebou pozpátku.  

**Řešení:**  
```python
text = input("Zadej text: ").replace(" ", "").lower()
if text == text[::-1]:
    print("Text je palindrom.")
else:
    print("Text není palindrom.")
```

---

### **8. Hra - Hádej číslo**
**Úkol:**  
Vytvořte hru, kde program náhodně vybere číslo mezi 1 a 100. Hráč se pokouší číslo uhádnout a program mu dává nápovědu (větší/menší).  

**Postup:**  
1. Vygenerujte náhodné číslo.  
2. Opakovaně požádejte hráče o tip, dokud číslo neuhodne.  
3. Poskytněte nápovědu, zda je číslo větší nebo menší.  

**Řešení:**  
```python
import random

cislo = random.randint(1, 100)
while True:
    tip = int(input("Hádej číslo: "))
    if tip < cislo:
        print("Více!")
    elif tip > cislo:
        print("Méně!")
    else:
        print("Gratuluji, uhodl jsi číslo!")
        break
```

---

### **9. Počítadlo výskytů slov**
**Úkol:**  
Napište program, který spočítá počet výskytů jednotlivých slov v zadaném textu. Výstup zobrazte abecedně seřazený.  

**Postup:**  
1. Požádejte uživatele o zadání textu.  
2. Rozdělte text na jednotlivá slova.  
3. Použijte slovník k uložení četnosti každého slova.  
4. Výstup seřaďte podle klíčů.  

**Řešení:**  
```python
text = input("Zadej text: ").lower()
slova = text.split()
statistika = {}

for slovo in slova:
    statistika[slovo] = statistika.get(slovo, 0) + 1

for slovo, pocet in sorted(statistika.items()):
    print(f"{slovo}: {pocet}")
```

---

### **10. Záznamy o studentech (Seznamy a třídění)**
**Úkol:**  
Vytvořte program pro správu seznamu studentů. Každý student má jméno a známku. Program umožní přidání studenta, zobrazení seznamu a seřazení podle známky.  

**Postup:**  
1. Uložte studenty do seznamu jako dvojice (jméno, známka).  
2. Implementujte funkce pro přidání studenta a zobrazení seznamu.  
3. Umožněte řazení podle známek.  

**Řešení:**  
```python
studenti = []

while True:
    print("\nMožnosti: \n1 - Přidat studenta\n2 - Zobrazit seznam\n3 - Seřadit podle známky\n4 - Konec")
    volba = input("Vyber možnost: ")

    if volba == '1':
        jmeno = input("Zadej jméno studenta: ")
        znamka = float(input("Zadej známku: "))
        studenti.append((jmeno, znamka))
    elif volba == '2':
        for jmeno, znamka in studenti:
            print(f"{jmeno}: {znamka}")
    elif volba == '3':
        studenti.sort(key=lambda x: x[1])
        print("Seznam seřazen podle známek.")
    elif volba == '4':
        break
    else:
        print("Neplatná volba.")
```

---



"""
# ### **1. Kalkulačka (Základy výpočtů)**
# """**Úkol:**  
# Vytvořte program, který funguje jako jednoduchá kalkulačka. Uživateli umožní zadat dvě čísla a
# vybrat matematickou operaci (+, -, *, /). Program provede požadovaný výpočet a zobrazí výsledek.  

# **Postup:**  
# 1. Požádejte uživatele o zadání dvou čísel.  
# 2. Zeptejte se na typ operace, kterou chce provést.  
# 3. Použijte podmínky (if/elif) k provedení výpočtu.  
# 4. Ošetřete chybu při dělení nulou.  
# 5. Zobrazte výsledek nebo chybovou zprávu.  
# """
# prvni_cislo = float(input("Zadej první číslo: "))
# druhe_cislo = float(input("Zadej druhé číslo: "))
# operace = input("Zvol operaci - ,+, ,-, ,*, ,/,: ")

# if operace == "+":
#     print(f"Sčítání: {prvni_cislo + druhe_cislo}")
# elif operace == "-":
#     print(f"Odčítání: {prvni_cislo - druhe_cislo}")
# elif operace == "*":
#     print(F"Násobení: {prvni_cislo * druhe_cislo}")
# else:
#     if druhe_cislo > 0:
#         print(f"Dělení: {prvni_cislo / (druhe_cislo)}")
#     else:
#         print("Nulou nelze dělit")

# -------------------------------------------------------------------------------------------------

## **2. Správa kontaktů (Práce se slovníky)**
"""
**Úkol:**  
Vytvořte program pro správu kontaktů. Program umožní uživateli přidat nový kontakt, 
odebrat existující kontakt a zobrazit všechny kontakty.  

**Postup:**  
1. Použijte slovník pro uložení jmen a telefonních čísel.  
2. Vytvořte cyklus, který umožní opakované zadávání příkazů.  
3. Implementujte možnosti pro přidání, odstranění a zobrazení kontaktů, následně export do txt. souboru.  
4. Ošetřete chyby, například neexistující kontakt.  
"""

kontakty = []

while True:
    print("#" * 20)
    print("")
    print("Možnosti: \n1 - přidej kontakt \n2 - odstranění kontaktu \n3 - zobrazení všech kontaktů \n4 - konec")
    volba = input("Zadej volbu: ")
    print("#" * 20)
    print("")

    if volba == "1":
        jmeno = input("Zadej jméno: ")
        cislo = input("Zadej číslo: ")
        email = input("Zadej email: ")
        kontakt = {
            "Jméno": jmeno,
            "Číslo": cislo,
            "Email": email
            }
        kontakty.append(kontakt)
        print(f"Kontakt přidán: {jmeno} : {cislo} : {email}")
    
    elif volba == "2":
        jmeno = input("Zadej jméno ke smazání: ")
        smazan = False
        for kontakt in kontakty[:]:  # Procházej kopii seznamu
            if kontakt["Jméno"] == jmeno:
                kontakty.remove(kontakt)
                smazan = True
                print(f"Kontakt {jmeno} smazán!")
                break
        if not smazan:
            print("Kontakt není v databázi.")
        

    elif volba == "3":
        export = input("Pro zobrazení slovníku zadej 1, pro export do txt. zadej 2: ")
        if export == "1":
            for kontakt in kontakty:
                print(f"Jméno: {kontakt['Jméno']} : Číslo: {kontakt['Číslo']} : Email: {kontakt['Email']}\n")
        else:
            with open("export_seznam.txt", "w") as file:
                for kontakt in kontakty: 
                    file.write(f"Jméno: {kontakt['Jméno']} : Číslo: {kontakt['Číslo']} : Email: {kontakt['Email']}\n")
            print("Soubor exportován")
    
    elif volba == "4":
        print("Končím program. Díky za použití.")
        break

    else:
        print("Neplatné zadání.")