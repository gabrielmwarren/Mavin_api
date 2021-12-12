import requests
from requests.structures import CaseInsensitiveDict
from json import loads

print("What type of card are you searching for")
print("1. Football")
print("2. Pokemon")
print(" ")

card_types = input("Pick 1 - 2: ")


if card_types == "1":
    year = input('Year Card Was Made: ')
    name1 = input('Players First Name (No Spaces): ')
    name2 = input('Players Last Name (No Spaces): ')
    company = input("Card Manufacturer (No Spaces): ")
    number = input('Card Number: ')

    url = "https://api.mavin.io/search?q=" + str(year) + "%20" + str(name1) + "%20" + str(name2) + "%20" + str(company) + "%20" + str(number)

elif card_types == "2":
    po_name = input("Pokemon's Name (No Spaces): ")
    po_number_1 = input("Pokemon's 1st Number (No Spaces): ")
    po_number_2 = input("Pokemon's 2nd Number (No Spaces): ")

    url = "https://api.mavin.io/search?q=" + str(po_name) + "%20" + str(po_number_1) + "%2F" + str(po_number_2)

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["X-API-KEY"] = "b11a4c70-219e-4705-a02a-55f6df35244f"


resp = requests.get(url, headers=headers)

resp_content_json = resp._content
resp_content = loads(resp_content_json)
card_market_value = resp_content["marketValue"]
card_query = resp_content["query"]
low_value = resp_content["lowestValue"]
high_value = resp_content["highestValue"]
card_category = resp_content["category"]

print(" ")
print(" ")
print(card_query + ": " + card_category)
print(" ")
print("Avg. Price: " + card_market_value)
print("Lowest Price: " + low_value)
print("Highest Price: " + high_value)
