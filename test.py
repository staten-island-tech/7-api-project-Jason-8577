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
    print(f"{key.title()}: {value}") """


import requests

def getclass(Class):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{Class.lower()}")
    if response.status_code != 200:
        print("Error")
        return None
    
    data = response.json()
    return data

b = getclass("Barbarian")
B = getclass("Bard")
c = getclass("Cleric")
d = getclass("Druid")
f = getclass("Fighter")
m = getclass("Monk")
p = getclass("Paladin")
r = getclass("Ranger")
R = getclass("Rogue")
s = getclass("Sorcerer")
w = getclass("Warlock")
W = getclass("Wizard")

import tkinter as tk

def imports():
    for key, value in W.items():              #Change the () or letter according to class {for key, value in ().items():}
        print(f"{key.title()}: {value}")

window = tk.Tk()
window.title("Dnd")
my_button = tk.Button(
window, 
text = "Class imports",
command = imports,
font = ("Arial", 16),
bg = "darkblue",
fg = "white",
relief = "raised",
padx = 10, pady = 5
)

my_button.pack(pady=20)
window.mainloop()