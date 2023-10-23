from .base import *
from .low_price_request import get_low_price_response
from .high_price_request import get_high_price_response
from .best_deal_request import get_best_deal_response


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=0))
def date_in_calendar(callback_query):
    chat_id = callback_query.message.chat.id
    user = user_dict[chat_id]

    result, key, step = DetailedTelegramCalendar(calendar_id=0,
                                                 min_date=date.today(),
                                                 locale='ru').process(callback_query.data)
    if not result and key:
        bot.edit_message_text('Выберите дату въезда',
                              chat_id,
                              callback_query.message.message_id,
                              reply_markup=key)
    elif result:
        user.date_in = result
        bot.edit_message_text(f'Дата въезда {result}',
                              chat_id,
                              callback_query.message.message_id)
        date_out(callback_query.message)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def date_out_calendar(callback_query):
    chat_id = callback_query.message.chat.id
    user = user_dict[chat_id]

    result, key, step = DetailedTelegramCalendar(calendar_id=1,
                                                 min_date=user.date_in +
                                                 timedelta(days=1),
                                                 locale='ru').process(callback_query.data)
    if not result and key:
        bot.edit_message_text('Выберите дату выезда',
                              chat_id,
                              callback_query.message.message_id,
                              reply_markup=key)
    elif result:
        user.date_out = result
        bot.edit_message_text(f'Дата выезда {result}',
                              chat_id,
                              callback_query.message.message_id)
        msg = bot.send_message(chat_id, 'Нужны ли вам фотографии? +/-')
        bot.register_next_step_handler(msg, process_photo_step,)


def date_in(message):
    """data out"""
    calendar, step = DetailedTelegramCalendar(calendar_id=0,
                                              min_date=date.today(),
                                              locale='ru').build()
    bot.send_message(message.chat.id,
                     'Выберите дату въезда',
                     reply_markup=calendar)


def date_out(message):
    """'data in"""
    chat_id = message.chat.id
    user = user_dict[chat_id]

    calendar, step = DetailedTelegramCalendar(calendar_id=1,
                                              min_date=user.date_in +
                                              timedelta(days=1),
                                              locale='ru').build()
    bot.send_message(message.chat.id,
                     'Выберите дату выезда',
                     reply_markup=calendar)


def process_city_step(message):
    """chose city pro"""
    chat_id = message.chat.id
    city = message.text
    user = user_dict[chat_id]
    user.city = city
    msg = bot.reply_to(message, 'how many hotel you wanna see?(not many 5)')
    bot.register_next_step_handler(msg, process_lin)


def process_lin(message):
    """"response numbers hotel"""
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.list_len = message.text
    if user.key_request[1:] == 'best_deal':
        msg = bot.reply_to(message, 'input min(price)')
        bot.register_next_step_handler(msg, process_price_long)
    else:
        date_in(message)


def process_price_long(message):
    """mix(price),max(price),max_long(too city centre)"""
    chat_id = message.chat.id
    user = user_dict[chat_id]
    print(user.price_long, "flag")
    if not user.price_long:
        user_dict[chat_id].price_long = [message.text]
        msg = bot.reply_to(message, 'input max(price)')
        bot.register_next_step_handler(msg, process_price_long)
    elif len(user.price_long) == 1:
        user_dict[chat_id].price_long.append(message.text)
        msg = bot.reply_to(message, 'max_long(too city centre)')
        bot.register_next_step_handler(msg, process_price_long)
    else:
        user_dict[chat_id].price_long.append(message.text)
        date_in(message)


def process_photo_step(message):
    """"photo upload"""
    if message.text == '+':
        msg = bot.reply_to(message, 'how many?')
        bot.register_next_step_handler(msg, process_photo_step)
    else:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.photos = message.text
        price_key = user.key_request
        if price_key[1:] == 'high_price':
            get_high_price_response(user, chat_id)
        elif price_key[1:] == 'low_price':
            get_low_price_response(user, chat_id)
        else:
            get_best_deal_response(user, chat_id)


def process_history_step(message):
    """process too history"""
    chat_id = message.chat.id
    start()
    return check_user_in_db(chat_id)
