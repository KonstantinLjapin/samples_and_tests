def set_power_limit(sequence: int, mode: int, interval_type: int, interval_value: int, limit_value: int) -> tuple:
    """устанавливает лимит мощности
    на вход принимает:
        sequence: номер запроса,
        mode: режим лимитирования,
        interval_type: тип интервала,
        interval_value: тип интервала,
        limit_value: int
    на выходе:
        type_of_report: тип отчёта
        reserv: резерв
        sequence: номер запроса
    """
    #фунционал
    return (type_of_report, reserv, sequence)

def get_power_limit(sequence: int) -> tuple:
    """получить значения заданного лимита мощности
    на вход принимает:
        sequence: номер запроса
    на выходе:
        type_of_report: тип отчёта,
        reserv: резерв,
        sequence: номер запроса,
        mode: режим лимитирования,
        interval_type: тип интервала,
        interval_value: значение интервала,
        limit_value: значение лимита
    """
    #фунционал
    return (type_of_report, reserv, sequence, mode,
            interval_type, interval_value, limit_value)

def set_relay_state(sequence: int, mode: int)  -> tuple:
    """ установить состояние реле
    на вход принимает:
        sequence: номер запроса,
        mode: режим реле
    на выходе:
        type_of_report: тип отчёта,
        reserv: резерв,
        sequence: номер запроса,
        mode: режим реле
    """
    #фунционал
    return (type_of_report, reserv, sequence, mode)

def get_relay_state(sequence: int) -> tuple:
    """ получить состояние реле
    на вход принимает:
        sequence: номер запроса,
    на выходе:
        type_of_report: тип отчёта,
        reserv: резерв,
        sequence: номер запроса,
        mode: режим реле
    """
    #фунционал
    return (type_of_report, reserv, sequence, mode)


get_relay_state(3)
# получаем состояние реле
set_relay_state(3, 10)
# устанавливаем его в положение вкл(10)
get_power_limit(3)
# получаем установленые лимиты мощности
set_power_limit(3, 1, 0, 2, 120)
# устанавливаем лимиты мощности
set_power_limit(3, 1, 0, 2, 0)
# сбрасываем лимиты мощности
get_relay_state(3)
# получаем состояние реле
set_relay_state(3, 9)
# устанавливаем его в положение выкл(9)


