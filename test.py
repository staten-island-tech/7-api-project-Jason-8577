""" import requests

def getclass(Class):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{Class.lower()}")
    if response.status_code != 200:
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "hit_die": data["hit_die"],
        "subclasses": data["subclasses"],
        "starting_equipment": data["starting_equipment"],
        "proficiencies": data["proficiencies"],
    }

import tkinter as tk

window = tk.Tk()
window.title("DND Class information")
window.geometry("450x400")
window.resizable(False, False)

prompt = tk.Label(window, text="Input a DND class:", font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=25)
entry.pack(pady=5)

result_frame = tk.Frame(window)
result_frame.pack(pady=15)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Arial", 11),
    justify="left",
    wraplength=420
)
result_label.pack()

def show_class():
    dnd = getclass(entry.get())

    if not dnd:
        result_label.config(text="Class Not Found!")    
        return

    text = ""
    for key, value in dnd.items():
        text += f"{key.title()}: {value}\n\n"

    result_label.config(text=text)
    
btn = tk.Button(window, text="Show Class Info", font=("Arial", 14), command=show_class)
btn.pack(pady=10)

window.mainloop() """



import requests
import tkinter as tk

def getclass(Class):
    response = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{Class.lower()}")
    if response.status_code != 200:
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "hit_die": data["hit_die"],
        "subclasses": data["subclasses"],
        "starting_equipment": data["starting_equipment"],
        "proficiencies": data["proficiencies"],
    }

window = tk.Tk()
window.title("DND Class Information")
window.geometry("450x600")
window.resizable(False, False)

prompt = tk.Label(window, text="Input a DND class:", font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=25)
entry.pack(pady=5)

result_frame = tk.Frame(window)
result_frame.pack(pady=15, fill="both", expand=True)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_text = tk.Text(
    result_frame,
    font=("Arial", 11),
    wrap="word",
    yscrollcommand=scrollbar.set
)
result_text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=result_text.yview)

def show_class():
    dnd = getclass(entry.get())
    result_text.delete("1.0", tk.END) 

    if not dnd:
        result_text.insert(tk.END, "Class Not Found!")
        return

    text = ""
    for key, value in dnd.items():
        text += f"{key.title()}: {value}\n\n"

    result_text.insert(tk.END, text)
    
reverse_button = tk.Button(window, text="DND Class Information",
font=("Arial", 14),

command=show_class)

reverse_button.pack(pady=15)

window.mainloop()