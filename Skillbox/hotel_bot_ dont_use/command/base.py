import os
import sys
from datetime import date, timedelta
import telebot
from telegram_bot_calendar import DetailedTelegramCalendar
from dotenv import load_dotenv, find_dotenv
from .models import *
from telebot import types
if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

user_dict = {}


class User:
    def __init__(self, key_request, chat_id):
        self.key_request = key_request
        self.chat_id = chat_id
        self.city = None
        self.list_len = None
        self.price_long = None
        self.date_in = None
        self.date_out = None
        self.photos = None


def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])


if __name__ == '__main__':
    pass
