import random as rnd
CARDS = [
    "Eso pikové", "2 pikové", "3 pikové", "4 pikové", "5 pikové", "6 pikové", "7 pikové", "8 pikové", "9 pikové", "10 pikové", "Spodek pikový", "Svršek pikový", "Král pikový",
    "Eso srdcové", "2 srdcové", "3 srdcové", "4 srdcové", "5 srdcové", "6 srdcové", "7 srdcové", "8 srdcové", "9 srdcové", "10 srdcové", "Spodek srdcový", "Svršek srdcový", "Král srdcový",
    "Eso kárové", "2 kárové", "3 kárové", "4 kárové", "5 kárové", "6 kárové", "7 kárové", "8 kárové", "9 kárové", "10 kárové", "Spodek kárový", "Svršek kárový", "Král kárový",
    "Eso křížové", "2 křížové", "3 křížové", "4 křížové", "5 křížové", "6 křížové", "7 křížové", "8 křížové", "9 křížové", "10 křížové", "Spodek křížový", "Svršek křížový", "Král křížový"
]

def hod_minci() -> str:
    
    hod = rnd.randint(0,1)
    if hod == 1:
        return "Panna"
    else:
        return "Orel"

def hod_kostkou(pocet_stran: int, pocet_hodu: int = 1) -> int:
    sum = 0
    for hod in range(pocet_hodu):
        sum+= rnd.randint(1, pocet_stran)
    return sum

def nahodna_karta() -> str:
    index = rnd.randint(0, len(CARDS) - 1)
    return CARDS[index]