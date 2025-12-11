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


""" import requests

def getclass(Class):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{Class.lower()}")
    if response.status_code != 200:
        print("Error")
        return None
    
    data = response.json()
    return data

dnd = getclass("Druid")
for key, value in dnd.items():
    print(f"{key.title()}: {value}")


import requests

def getclass(Class):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{Class.lower()}")
    if response.status_code != 200:
        print("Error")
        return None
    
    data = response.json()
    return {
        "index": data["index"],
        "name": data["name"],
        "url": data["url"]
    }

dnd = getclass("barbarian")
for key, value in dnd.items():
    print(f"{key.title()}: {value}") """

"""     https://www.dnd5eapi.co/ """



import tkinter as tk

window = tk.Tk()
window.title("Message Reverser")
window.geometry("400x250")
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)

def reverse_message():
    text = entry.get()
    reversed_text = text[::-1]
    result_label.config(text=f"Backwards: {reversed_text}")

reverse_button = tk.Button(window, text="Reverse Message!",
font=("Arial", 14),

command=reverse_message)

reverse_button.pack(pady=10)