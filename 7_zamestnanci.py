# seznam
zamestnanci = ["František", "Anna", "Jakub", "Klára"]


zamestnanci_a = zamestnanci.copy()

print(zamestnanci_a)
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")

print("Nová jména přidána: ", zamestnanci_a)

zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")
print("Nová jména vložena: ", zamestnanci_b)

