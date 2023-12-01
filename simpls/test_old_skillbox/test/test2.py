import json
import requests

url = "https://hotels4.p.rapidapi.com/properties/v2/list"

citi = "2621"
payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "destination": {"regionId": citi},
    "checkInDate": {
        "day": 10,
        "month": 10,
        "year": 2023
    },
    "checkOutDate": {
        "day": 15,
        "month": 10,
        "year": 2023
    },
    "rooms": [
        {
            "adults": 2,
            "children": [{"age": 5}, {"age": 7}]
        }
    ],
    "resultsStartingIndex": 0,
    "resultsSize": 30,
    "sort": "PRICE_HIGH_LOW_TO",
    "filters": {"price": {
        "max": 200,
        "min": 1
    }}
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "KEY",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
temp = json.loads(response.text.encode().decode('utf-8-sig'))
print(type(temp))
list_hotel_dict = temp["data"]["propertySearch"]["properties"]
print(type(list_hotel_dict))
print(type(list_hotel_dict[0]))
for hotel in list_hotel_dict:
    print(hotel["name"], hotel["price"]["lead"]["formatted"])
with open('for_parce_properties.json', 'w', encoding='utf-8') as s:
    json.dump(temp, s, indent=4)
    print('ok')
