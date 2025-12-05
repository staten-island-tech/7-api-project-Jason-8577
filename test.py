""" import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Charizard")
for key, value in pokemon.items():
    print(f"{key.title()}: {value}")"""


import requests

def info(search):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/{search.lower()}")
    if response.status_code != 400:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return{
        "name": data["name"]
    }
dnd = info("acid arrow")
for key, value in dnd.items():
    print(f"{key.title()}: {value}")
    
