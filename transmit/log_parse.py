from datetime import datetime, timedelta, date
from pathlib import Path, PurePath


def read_log(path):
    count_day: int = 5
    now: datetime = datetime.now()
    day: int = int(now.date().day)
    list_data: list = [str(date(day=day-i, year=now.year, month=now.month)) for i in range(1, count_day+1)]
    with open(path, 'r', encoding='utf-8') as f:
        print(f.readline().split(' '))
        for temp in f:
            for i in temp:
                if i in list_data:
                    print(temp)
    print(str(date(year=now.year, month=now.month, day=now.day)))
    print(list_data)


def puke_path(temp):
    return list(Path(PurePath(*list(PurePath(Path.cwd()).parts)[:-2])).glob(f'**/{temp}.log'))[0]


d = 'debug'
e = 'error'
print(puke_path(d))

print()

read_log(puke_path(e))


