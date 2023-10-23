from .base import *
from .calendar_and_steps import process_city_step, process_history_step


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """command send_welcome"""
    bot.reply_to(message, f"/low_price\n" 
                          f"/high_price\n" 
                          f"/best_deal\n" 
                          f"/history\n")


@bot.message_handler(commands=['high_price'])
def high_price(message):
    """command high_price"""
    msg = bot.reply_to(message, 'chose city')
    user_start(message)
    bot.register_next_step_handler(msg, process_city_step)


@bot.message_handler(commands=['best_deal'])
def best_deal(message):
    """command best_deal"""
    msg = bot.reply_to(message, 'chose city')
    user_start(message)
    bot.register_next_step_handler(msg, process_city_step)


@bot.message_handler(commands=['low_price'])
def low_price(message):
    """command low_price"""
    msg = bot.reply_to(message, 'chose city')
    user_start(message)
    bot.register_next_step_handler(msg, process_city_step)


@bot.message_handler(commands=['history'])
def history(message):
    """command history"""
    user_start(message)
    temp, some = process_history_step(message)
    bot.send_message(message.chat.id, some)
    if temp.urls_photo != '-':
        medias = [
            types.InputMediaPhoto(media, caption=temp.intermediat)
            if index == 0 else types.InputMediaPhoto(media) for index, media in enumerate(temp.urls_photo.split(','))]
        bot.send_media_group(message.chat.id, medias)
    else:
        bot.send_message(message.chat.id, temp.intermediat)


def user_start(message):
    """start user class"""
    chat_id = message.chat.id
    user = User(message.text, chat_id)
    user_dict[chat_id] = user


if __name__ == '__main__':
    pass
