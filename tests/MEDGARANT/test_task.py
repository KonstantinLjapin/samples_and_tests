import datetime
from pprint import pprint

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


def returner_template_dict(s: datetime.timedelta, e: datetime.timedelta) -> dict:
    template_dict_time: dict = {start_key_world: '',
                                stop_key_world: ''}
    template_dict_time.update({start_key_world: s})
    template_dict_time.update({stop_key_world: e})
    return template_dict_time


def returner_dec_time(date_time_str: str) -> datetime.datetime.time:
    return datetime.datetime.strptime(date_time_str, '%H:%M').time()


def returner_time_delta(date_time_str: str) -> datetime.timedelta:
    return datetime.timedelta(hours=returner_dec_time(date_time_str).hour,
                              minutes=returner_dec_time(date_time_str).minute)


def time_denominator(start: datetime.timedelta = returner_time_delta(work_start),
                     end: datetime.timedelta = returner_time_delta(work_end),
                     cell: datetime.timedelta = returner_time_delta(half_life_hour)) -> list:
    """
    a = returner_dec_time(work_start)
    b = returner_dec_time(work_end)
    c = (datetime.timedelta(hours=a.hour, minutes=a.minute)
     + datetime.timedelta(hours=returner_dec_time(half_life_hour).hour,
                          minutes=returner_dec_time(half_life_hour).minute))
    :param start: datetime.datetime.time
    :param end: datetime.datetime.time
    :param cell: datetime.datetime.time
    :return: list
    """
    s_temp: datetime.timedelta = start
    e_temp: datetime.timedelta = start + cell
    out_list: list = []
    while True:
        for t in out_list:
            if end in t.values():
                return out_list
        l_t: dict = returner_template_dict(s_temp, e_temp)
        out_list.append(l_t)
        s_temp: datetime.timedelta = e_temp
        e_temp: datetime.timedelta = s_temp + cell


def printer_list_space(space_list: list):
    for i in space_list:
        s_td = i.get(start_key_world)
        e_td = i.get(stop_key_world)
        sdt = datetime.datetime.strptime(str(s_td), "%H:%M:%S")
        edt = datetime.datetime.strptime(str(e_td), "%H:%M:%S")
        print(sdt.hour, ":", sdt.minute, "start")
        print(edt.hour, ":", edt.minute, "end")
        print("-")


def cuter_busy_list() -> list:
    out_list: list = []
    for t in busy:
        s_t: datetime.timedelta = returner_time_delta(t.get(start_key_world))
        e_t: datetime.timedelta = returner_time_delta(t.get(stop_key_world))
        space_list: list = time_denominator()
        for s in space_list:
            s_td = s.get(start_key_world)
            e_td = s.get(stop_key_world)
            if (s_td > s_t and s_td >= e_t) or (e_td <= s_t and e_td < e_t):
                out_list.append(s)
    return out_list


printer_list_space(cuter_busy_list())


