""" import requests

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
    for key, value in W.items():
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
window.mainloop()  """




import requests

def getclass(Class):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{Class.lower()}")
    if response.status_code != 200:
        print("Error")
        return None
    
    data = response.json()
    return data

print("Click on Description to get the names of all classes.")

import tkinter as tk

window = tk.Tk()
window.title("DND")
window.geometry("400x250") 
window.resizable(False, False) 
prompt = tk.Label(window, text="Input a Class below:",
font=("Arial", 14))
prompt.pack(pady=10) 

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)

def Class_dnd():
    dnd = getclass(f"{entry.get()}")
    for key, value in dnd.items():
        print(f"{key.title}: {value}")

Class_def = tk.Button(window, text = "Description",
font = ("Arial", 14),

command = Class_dnd)
Class_def.pack(pady = 10)
window.mainloop()
