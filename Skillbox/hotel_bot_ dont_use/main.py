from command.base import *
from command.price import *
from command.calendar_and_steps import *


def register_all_handlers(message):
    send_welcome(message)
    low_price(message)
    high_price(message)
    best_deal(message)
    history(message)
    process_city_step(message)
    date_in(message)
    date_out(message)
    process_photo_step(message)
    process_history_step(message)
    process_lin(message)


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()
