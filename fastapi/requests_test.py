import requests

BASE_URL = "http://127.0.0.1:8000"

def test_base():
    response = requests.get(BASE_URL)
    data = response.json()
    print(data["message"])

def test_card():
    response = requests.get(BASE_URL + "/card")
    print(response.text)

def test_coin():
    response = requests.get(BASE_URL + "/coin")
    print(response.text)

def test_dice_1():
    params = {"dice_sides": 6}
    response = requests.get(BASE_URL + "/dice", params=params)
    print(response.text)

test_dice_1()