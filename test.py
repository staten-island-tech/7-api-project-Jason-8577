""" https://opentdb.com/api_config.php """

import requests

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
    print(f"{key.title()}: {value}")
    

import requests

def trivia_questions(questions):
    response = requests.get(f"https://opentdb.com/api.php?amount=10&category=15&type=multiple{questions.lower()}") 
    if response.status_code != 200:
        print("Error fetching data!")
        return None
        
    data = response.json()
    return data
    
trivia = trivia_questions("easy")
print(trivia)
    