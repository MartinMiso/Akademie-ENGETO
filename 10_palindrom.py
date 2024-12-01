palindrom = input("Zadej palindrom: \n")
#print(palindrom)
veta = ""

for pismeno in palindrom:
    veta += pismeno #+ veta

#print(veta)

if palindrom == veta:
    print("Ano, je to palindrom")
else:
    print("Ne, není to palindrom")

"""nebo taky takto"""

pozpatku = palindrom[::-1]
if palindrom == pozpatku:
     print("Ano, je to palindrom")
else:
    print("Ne, není to palindrom")
