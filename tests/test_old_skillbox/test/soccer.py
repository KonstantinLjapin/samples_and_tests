import json
import requests

def get_leagues():
    url = "https://livescore6.p.rapidapi.com/leagues/v2/list"
    querystring = {"Category": "soccer"}
    headers = {        "X-RapidAPI-Key": "KEY",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"    }
    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text.encode().decode('utf-8-sig'))
    with open('soccer.json', 'w', encoding='utf-8') as s:
        json.dump(data, s, indent=4)
        print('ok')

def main():
    get_leagues()
if __name__ == '__main__':    main()