import requests
from requests.structures import CaseInsensitiveDict
from json import loads
import tkinter as tk
from tkinter import Entry, ttk

window = tk.Tk()


window.tk.call("source", "/home/pi/Dev/Azure-ttk-theme/azure.tcl")
window.tk.call("set_theme", "light")




def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


def football_url_get():
    football_cards_info_list = football_cards.info.get().split(" ")

    url = "https://api.mavin.io/search?q="

# %20

    for i in range(len(football_cards_info_list)):
        url = url + "%20" + football_cards_info_list[i]

    print(url)

    football_url_get.url = url

    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["X-API-KEY"] = ""



    if football_cards.is_football:
        url = football_url_get.url
    else:
        url = pokemon_cards.url

    resp = requests.get(url, headers=headers)

    resp_content_json = resp._content
    resp_content = loads(resp_content_json)
    card_market_value = resp_content["marketValue"]
    card_query = resp_content["query"]
    low_value = resp_content["lowestValue"]
    high_value = resp_content["highestValue"]
    card_category = resp_content["category"]

    card_query_lbl = tk.Label(text=card_query + ": " + card_category)
    price_avg_lbl = tk.Label(text="Avg. Price: " + card_market_value)
    low_price_lbl = tk.Label(text="Lowest Price: " + low_value)
    high_price_lbl = tk.Label(text="Highest Price: " + high_value)

    card_query_lbl.pack()
    price_avg_lbl.pack()
    low_price_lbl.pack()
    high_price_lbl.pack()


def pokemon_url_get():
    pokemon_cards_info_list = pokemon_cards.info.get().split(" ")

    url = "https://api.mavin.io/search?q="

    for i in range(len(pokemon_cards_info_list)):
        if i == len(pokemon_cards_info_list):
            url = url + "%2F" + pokemon_cards_info_list[i]
        else:
            url = url + "%20" + pokemon_cards_info_list[i]

    print(url)

    pokemon_cards.url = url

    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["X-API-KEY"] = ""



    if football_cards.is_football:
        url = football_url_get.url
    else:
        url = pokemon_cards.url

    resp = requests.get(url, headers=headers)

    resp_content_json = resp._content
    resp_content = loads(resp_content_json)
    card_market_value = resp_content["marketValue"]
    card_query = resp_content["query"]
    low_value = resp_content["lowestValue"]
    high_value = resp_content["highestValue"]
    card_category = resp_content["category"]

    card_query_lbl = tk.Label(text=card_query + ": " + card_category)
    price_avg_lbl = tk.Label(text="Avg. Price: " + card_market_value)
    low_price_lbl = tk.Label(text="Lowest Price: " + low_value)
    high_price_lbl = tk.Label(text="Highest Price: " + high_value)

    card_query_lbl.pack()
    price_avg_lbl.pack()
    low_price_lbl.pack()
    high_price_lbl.pack()




def football_cards():
    football_cards.is_football = True
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=6)
    frm_form.pack()


    intro_lbl =tk.Label(master=frm_form, text="Card Information:")
    intro_lbl.grid(row=0, column=1)

    
    info_lbl = tk.Label(master=frm_form, text="")
    football_cards.info = tk.Entry(master=frm_form, width=50,)
    football_cards.info.insert(0, "year + name + company + number")
    info_lbl.grid(row=2, column=0, sticky="e")
    football_cards.info.grid(row=2, column=1)


    frm_buttons = tk.Frame(relief=tk.RAISED, borderwidth=3)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_submit = tk.Button(master=frm_buttons, text="Enter", command=football_url_get)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


    





def pokemon_cards():
    football_cards.is_football = False
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=6)
    frm_form.pack()


    intro_lbl =tk.Label(master=frm_form, text="Card Information:")
    intro_lbl.grid(row=0, column=1)

    
    info_lbl = tk.Label(master=frm_form, text="")
    pokemon_cards.info = tk.Entry(master=frm_form, width=50,)
    pokemon_cards.info.insert(0, "name + number")
    info_lbl.grid(row=2, column=0, sticky="e")
    pokemon_cards.info.grid(row=2, column=1)


    frm_buttons = tk.Frame(relief=tk.RAISED, borderwidth=3)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_submit = tk.Button(master=frm_buttons, text="Enter", command=pokemon_url_get)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)




greetings_frm = tk.Frame()
greetings_frm.pack(ipady=5)


greeting = tk.Label(master=greetings_frm, text="Hello, What Type Of Card Are You Searching For?")
button_football = tk.Button(
    text="Football",
    width=25,
    height=5,
    bg="brown",
    fg="white",
    command=football_cards,
)

button_pokemon = tk.Button(
    text="Pokemon",
    width=25,
    height=5,
    bg="yellow",
    fg="red",
    command=pokemon_cards,
)

greeting.pack()
button_football.pack(side=tk.LEFT,)
button_pokemon.pack(side=tk.RIGHT,)








window.mainloop()




