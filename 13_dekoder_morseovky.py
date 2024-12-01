# co chceme dekódovat
sifrovana_zprava = ".-.. . --- -. .- .-. -.. ---"
print(f"Původní zpráva: {sifrovana_zprava}")
# dekodovaná zpráva
zprava = ""

# vzorová sekvence
abecedni_znaky =  "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

# rozdělení zprávy na znaky morseovky
znaky = sifrovana_zprava.split(" ")
print("Znaky")
print(znaky)

# interace morseovky
for morseuv_znak in znaky:
    abecedni_znak = "?"
    try:
        index = morseovy_znaky.index(morseuv_znak)
        abecedni_znak = abecedni_znaky[index]
        zprava += abecedni_znak
    except ValueError: #znak nenalezen
        zprava += abecedni_znak

print(f"Dekódovaná zpráva je: {zprava}")


""" DEKODÉR"""
input()
# co chceme dekódovat
sifrovana_zprava = "l e o n a r d"
print(f"Původní zpráva: {sifrovana_zprava}")
# dekodovaná zpráva
zprava = ""

# vzorová sekvence
abecedni_znaky =  "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

# rozdělení zprávy na znaky morseovky
znaky = sifrovana_zprava.split(" ")
print("Znaky")
print(znaky)

# interace morseovky
for abecedni_znak in znaky:
    morseuvic_znak = "?"
    try:
        index = abecedni_znaky.index(abecedni_znak)
        morseuvic_znak = morseovy_znaky[index]
        zprava += morseuvic_znak
    except ValueError: #znak nenalezen
        zprava += morseuvic_znak

print(f"Dekódovaná zpráva je: {zprava}")

