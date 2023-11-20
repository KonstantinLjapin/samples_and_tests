import datetime

import time
"""Тестовое задание

Доктор принимает с 9 утра до 9 вечера.
Часть времени у него занята: приемы, обед, уборка кабинета.
busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

Требуется сформировать список свободных окон по 30 минут.

"""

busy: list[dict] = [
    {'start': '10:30',
     'stop': '10:50'
     },
    {'start': '18:40',
     'stop': '18:50'
     },
    {'start': '14:40',
     'stop': '15:50'
     },
    {'start': '16:40',
     'stop': '17:20'
     },
    {'start': '20:05',
     'stop': '20:20'
     }
]
start_key_world: str = 'start'
stop_key_world: str = 'stop'
work_start: str = '9:00'
work_end: str = '21:00'
half_life_hour: str = '00:30'


def returner_templete_dict(s: datetime.datetime.time, e: datetime.datetime.time) -> dict:
    template_dict_time: dict = {start_key_world: '',
                                stop_key_world: ''}
    template_dict_time.update({start_key_world: s})
    template_dict_time.update({stop_key_world: e})
    return template_dict_time


def returner_dec_time(date_time_str: str) -> datetime.datetime.time:
    return datetime.datetime.strptime(date_time_str, '%H:%M').time()


def time_denominator(start: datetime.datetime.time = returner_dec_time(work_start),
                     end: datetime.datetime.time = returner_dec_time(work_end),
                     cell: datetime.datetime.time = returner_dec_time(half_life_hour)) -> list:

    out_list: list = []
    while True:
        for t in out_list:
            if end in t.values():
                return out_list
            cur_t: datetime.datetime.time = t.get(work_end)
            #temp_obj: dict = template_dict_time.update(start_key_world, cur_t, None)


print('Время:', returner_dec_time(work_start))
print(returner_templete_dict(returner_dec_time(work_start), returner_dec_time(work_end)))
print("OK")
