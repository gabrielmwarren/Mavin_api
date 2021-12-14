import requests
from requests.structures import CaseInsensitiveDict
from json import loads
import tkinter as tk
from tkinter import Entry, ttk

window = tk.Tk()


window.tk.call("source", "/home/pi/Dev/Azure-ttk-theme/azure.tcl")
window.tk.call("set_theme", "light")


def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if window.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        window.tk.call("set_theme", "light")
    else:
        # Set dark theme
        window.tk.call("set_theme", "dark")


def start():

    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    greetings_frm = tk.Frame()
    greetings_frm.pack(ipady=5)

    switch = ttk.Checkbutton(window, text='Dark Mode', style='Switch.TCheckbutton', command=change_theme)


    greeting = tk.Label(master=greetings_frm, text="Hello, What Type Of Card Are You Searching For?")
    button_football = tk.Button(
        text="Football",
        width=25,
        height=5,
        bg="brown",
        fg="gray",
        command=football_cards,
    )

    button_pokemon = tk.Button(
        text="Pokemon",
        width=25,
        height=5,
        bg="yellow",
        fg="gray",
        command=pokemon_cards,
    )

    greeting.pack()
    button_football.pack(side=tk.LEFT,)
    button_pokemon.pack(side=tk.RIGHT,)
    switch.pack(side=tk.RIGHT)




def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


def football_url_get():
    football_cards_info_list = football_cards.info.get().split(" ")

    url = "https://api.mavin.io/search?q="


    for i in range(len(football_cards_info_list)):

        if i == 0:
            url = url + football_cards_info_list[i]
        else:
            url = url + "%20" + football_cards_info_list[i]


    football_url_get.url = url

    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["X-API-KEY"] = "b11a4c70-219e-4705-a02a-55f6df35244f"



    if football_cards.is_football:
        url = football_url_get.url
    else:
        url = pokemon_cards.url

    resp = requests.get(url, headers=headers)

    info_frm = ttk.Frame()
    info_frm.pack()

    resp_content_json = resp._content

    try:
        resp_content = loads(resp_content_json)
    except:
        error_message = ttk.Label(master=info_frm, text="An Error Occurred Most Likely There Are No Matches For Your Search")
        continue_button_error = ttk.Button(master=info_frm, text="Continue", command=start)
        error_message.pack()
        continue_button_error.pack()


    card_market_value = resp_content["marketValue"]
    card_query = resp_content["query"]
    low_value = resp_content["lowestValue"]
    high_value = resp_content["highestValue"]
    card_category = resp_content["category"]

    card_query_lbl = ttk.Label(master=info_frm, text=card_query + ": " + card_category)
    price_avg_lbl = ttk.Label(master=info_frm, text="Avg. Price: " + card_market_value)
    low_price_lbl = ttk.Label(master=info_frm, text="Lowest Price: " + low_value)
    high_price_lbl = ttk.Label(master=info_frm, text="Highest Price: " + high_value)

    card_query_lbl.pack()
    price_avg_lbl.pack()
    low_price_lbl.pack()
    high_price_lbl.pack()

    frm_buttons = ttk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_contintue = ttk.Button(master=frm_buttons, text="Again", command=start)
    btn_contintue.pack(side=tk.RIGHT, padx=10, ipadx=10)


def pokemon_url_get():
    pokemon_cards_info_list = pokemon_cards.info.get().split(" ")

    url = "https://api.mavin.io/search?q="

    for i in range(len(pokemon_cards_info_list)):
        if i == len(pokemon_cards_info_list):
            url = url + "%2F" + pokemon_cards_info_list[i]
        else:
            url = url + "%20" + pokemon_cards_info_list[i]


    pokemon_cards.url = url

    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["X-API-KEY"] = "b11a4c70-219e-4705-a02a-55f6df35244f"



    if football_cards.is_football:
        url = football_url_get.url
    else:
        url = pokemon_cards.url

    resp = requests.get(url, headers=headers)

    resp_content_json = resp._content


    try:
        resp_content = loads(resp_content_json)
    except:
        error_message = ttk.Label(text="An Error Occurred Most Likely There Are No Matches For Your Search")
        continue_button_error = ttk.Button(text="Continue", command=start)
        error_message.pack()
        continue_button_error.pack()


    card_market_value = resp_content["marketValue"]
    card_query = resp_content["query"]
    low_value = resp_content["lowestValue"]
    high_value = resp_content["highestValue"]
    card_category = resp_content["category"]

    card_query_lbl = ttk.Label(text=card_query + ": " + card_category)
    price_avg_lbl = ttk.Label(text="Avg. Price: " + card_market_value)
    low_price_lbl = ttk.Label(text="Lowest Price: " + low_value)
    high_price_lbl = ttk.Label(text="Highest Price: " + high_value)

    card_query_lbl.pack()
    price_avg_lbl.pack()
    low_price_lbl.pack()
    high_price_lbl.pack()

    frm_buttons = ttk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_contintue = ttk.Button(master=frm_buttons, text="Again", command=start)
    btn_contintue.pack(side=tk.RIGHT, padx=10, ipadx=10)






def football_cards():
    football_cards.is_football = True
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()


    frm_form = ttk.Frame()
    frm_form.pack()


    intro_lbl =ttk.Label(master=frm_form, text="Card Information:")
    intro_lbl.grid(row=0, column=1)

    
    info_lbl = ttk.Label(master=frm_form, text="")
    football_cards.info = ttk.Entry(master=frm_form, width=50,)
    football_cards.info.insert(0, "year + name + company + number")
    info_lbl.grid(row=2, column=0, sticky="e")
    football_cards.info.grid(row=2, column=1)


    frm_buttons = ttk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_submit = ttk.Button(master=frm_buttons, text="Enter", command=football_url_get)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


    





def pokemon_cards():
    football_cards.is_football = False
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    frm_form = ttk.Frame()
    frm_form.pack()


    intro_lbl =ttk.Label(master=frm_form, text="Card Information:")
    intro_lbl.grid(row=0, column=1)

    
    info_lbl = ttk.Label(master=frm_form, text="")
    pokemon_cards.info = ttk.Entry(master=frm_form, width=50,)
    pokemon_cards.info.insert(0, "name + number")
    info_lbl.grid(row=2, column=0, sticky="e")
    pokemon_cards.info.grid(row=2, column=1)


    frm_buttons = ttk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_submit = ttk.Button(master=frm_buttons, text="Enter", command=pokemon_url_get)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)




start()


window.mainloop()




