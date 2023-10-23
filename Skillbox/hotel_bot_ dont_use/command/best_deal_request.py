import json
import re
import requests
from datetime import date


from .base import *

RAPID_TOKEN = os.environ.get('RAPID_TOKEN')


def get_best_deal_response(user: User, chat_id):
    bot.send_message(chat_id, 'work in')
    headers = {
        "X-RapidAPI-Key": RAPID_TOKEN,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    url_locations = "https://hotels4.p.rapidapi.com/locations/v3/search"
    querystring = {"q": user.city, "locale": "en_US", "langid": "1033", "siteid": "300000001"}
    response = requests.request("GET", url_locations, headers=headers, params=querystring)
    list_hotel = get_price(user, str(response))
    for obj in list_hotel:
        if user.photos.isdigit():
            medias = [
                types.InputMediaPhoto(media, caption=obj[0][0])
                if index == 0 else types.InputMediaPhoto(media) for index, media in enumerate(flatten(obj[1]))]
            bot.send_media_group(chat_id, medias)
        else:
            bot.send_message(chat_id, obj)
    try:
        start()
        data_base_con(user, list_hotel)
    except Exception as error:
        print(error)
    db.close()


def get_price(user: User, res: str):
    key = "gaiaId"
    gaiaId = ''.join(re.findall(r'\d+', (res[res.find(key):])[:res.find(",")]))
    url = "https://hotels4.p.rapidapi.com/properties/v2/list"
    citi = gaiaId
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": citi},
        "checkInDate": {
            "day": user.date_in.day,
            "month": user.date_in.month,
            "year": user.date_in.year
        },
        "checkOutDate": {
            "day": user.date_out.day,
            "month": user.date_out.month,
            "year": user.date_out.year
        },
        "rooms": [
            {
                "adults": 1
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": int(user.list_len),
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": int(user.price_long[1]),
            "min": int(user.price_long[0])
        }}
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_TOKEN,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    temp = json.loads(response.text.encode().decode('utf-8-sig'))
    list_hotel_dict = temp["data"]["propertySearch"]["properties"]
    list_longers = [meta["destinationInfo"]["distanceFromDestination"]["value"] for meta in list_hotel_dict]
    min_too_centr = list_longers.index(min(map(float, list_longers)))
    long = list_hotel_dict[min_too_centr]["destinationInfo"]["distanceFromDestination"]["value"]
    try:
        list_hotel_dict = list_hotel_dict[:long.index(int(user.price_long[2]))]
    except Exception as error:
        pass
    list_hotel_name_price = []
    for i in range(int(user.list_len)):
        description = get_pro_info(list_hotel_dict[i]["id"])
        if user.photos.isdigit():
            list_hotel_name_price += [[['\nname: ' + list_hotel_dict[i]["name"] + '\nDescription:' +
                                        '\nprice: ' + list_hotel_dict[i]["price"]["lead"]["formatted"]
                                        + '\nmile too centre: ' + str(long)
                                        + '\n\n' + description
                                        + '\nsite of full description:\n' + 'https://www.hotels.com/h'
                                        + list_hotel_dict[i]["id"] + '.Hotel-Information'], [
                                           get_image(list_hotel_dict[i]["id"], user.photos)]]]
        else:
            list_hotel_name_price += ['\nname: ' + list_hotel_dict[i]["name"] + '\nDescription:' +
                                      '\nprice: ' + list_hotel_dict[i]["price"]["lead"]["formatted"]
                                      + '\nmile too centre: ' + str(long)
                                      + '\n\n' + description
                                      + '\nsite of full description:\n' + 'https://www.hotels.com/h'
                                      + list_hotel_dict[i]["id"] + '.Hotel-Information']

    return list_hotel_name_price


def get_image(id_some, slice):
    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": id_some
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_TOKEN,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    temp = json.loads(response.text.encode().decode('utf-8-sig'))
    image_hotel_list = temp["data"]["propertyInfo"]["propertyGallery"]["images"]
    return flatten([image_url["image"]["url"] for image_url in image_hotel_list])[0:int(slice)]


def get_pro_info(id_some):
    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": id_some
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_TOKEN,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    temp = json.loads(response.text.encode().decode('utf-8-sig'))
    description_hotel = temp["data"]["propertyInfo"]["summary"]["location"]["whatsAround"]["editorial"]["content"]
    return description_hotel[0]


if __name__ == '__main__':
    pass
