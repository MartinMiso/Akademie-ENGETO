from fastapi import FastAPI, Form, Header, Response, APIRouter
from api.generator.generator import nahodna_karta, hod_kostkou, hod_minci

AUTH = "tajne"
router = APIRouter()


@router.get("/card")
async def card(auth : str = Header()):
    if auth != AUTH:
        Response(status_code=403, content="Not authorized")
    card = nahodna_karta()
    return {"card": card}

@router.get("/coin")
async def coin(auth: str = Header()):
    if auth != AUTH:
        Response(status_code=403, content="Not authorized")
    coin_throw = hod_minci()
    return {"coin_throw": coin_throw}

@router.get("/dice")
async def dice(dice_sides : int, throws: int = 1, auth: str = Header()):
    if auth != AUTH:
        Response(status_code=403, content="Not authorized")
    dice_throw = hod_kostkou(dice_sides, throws)
    return {"dice_throw": dice_throw}
