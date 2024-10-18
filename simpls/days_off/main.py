"""
Получение данных за день

https://isdayoff.ru/api/getdata?year=YYYY&month=MM&day=DD[&cc=xx&pre=[0|1]&covid=[0|1]]&sd=[0|1]

YYYY - год

ММ - месяц

DD - день

cc - код страны (по-умолчанию Россия)

pre - помечать сокращённые рабочие дни цифрой 2

covid - помечать рабочие дни цифрой 4 (в связи с пандемией COVID-19)

sd - считать, что неделя шестидневная

Возможные результаты

Ответ сервиса 	Значение 	Код возврата HTTP
0 	Рабочий день 	200
1 	Нерабочий день 	200
2 	Сокращённый рабочий день 	200
4 	Рабочий день 	200
100 	Ошибка в дате 	400
101 	Данные не найдены 	404
199 	Ошибка сервиса 	400
"""

import aiohttp
import asyncio


async def main():

    async with (aiohttp.ClientSession() as session):
        async with session.get(
                'https://isdayoff.ru/20241018'
        ) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html, "...")

asyncio.run(main())
