- https://github.com/eternnoir/pyTelegramBotAPI
- https://en.wikipedia.org/wiki/Child_process

t.me/my_shiny_skillbox_bot
name: my_shiny_bot
- unix machine
- $ sudo update && upgrade
- $ python3 -m venv myvenv
- $ pip install requirements.txt
- RUN
- sourse ../.. myvenv/bin/activate
- source .env __BOT-TOKEN
- or add sourse too venv
- python3 main_bot.py

- command /low_price - request minimal price
- command /high_price - request maximal price
- command /best_deal - add param min ad max price , long out centre
- command /history - last request description, intermedia 
