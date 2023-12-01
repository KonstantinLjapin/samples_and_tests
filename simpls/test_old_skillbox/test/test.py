import requests

url = "https://hotels4.p.rapidapi.com/locations/v3/search"

querystring = {"q": "new york", "locale": "en_US", "langid": "1033", "siteid": "300000001"}

headers = {
    "X-RapidAPI-Key": "KEY",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
with open('for_parce_locations.txt', 'w+') as s:
    temp = response.text
    s.write(str(temp))
    print(type(response.text))
