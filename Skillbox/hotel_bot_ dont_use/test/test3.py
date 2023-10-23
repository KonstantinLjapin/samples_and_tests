import json
import requests

url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "propertyId": "2223555"
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "7aa413d2fcmshe6bf0c0e564a302p10c977jsnbf96141b4a0e",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
temp = json.loads(response.text.encode().decode('utf-8-sig'))
print(type(temp))
image_hotel_list = temp["data"]["propertyInfo"]["propertyGallery"]["images"]
for image_url in image_hotel_list:
    print(image_url["image"]["url"])

with open('for_parce_properties_image.json', 'w', encoding='utf-8') as s:
    json.dump(temp, s, indent=4)
    print('ok')
