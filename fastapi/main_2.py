from fastapi import FastAPI, Header
from generator import hod_minci, nahodna_karta, hod_kostkou




app = FastAPI()

# 1. endpoint
@app.get("/")
def root():
    return "Moje nová API"

@app.get("/coin")
def coin():
    hod = hod_minci()
    return hod

@app.get("/card")
def card():
    return nahodna_karta()

@app.get("/dice")
def dice(pocet_stran: int, pocet_hodu: int = 1):
    sum = 0
    for _ in range (pocet_hodu):
        sum+= hod_kostkou(pocet_stran)
    return sum

@app.get("/card_auth")
def card(auth : str = Header()):
    if auth == "tajneHeslo":
        return nahodna_karta()