"""Первая строка содержит число n ( 1 ≤ n ≤ 100 ) – количество рядов в самолете.
 Далее в n строках вводится изначальная рассадка в самолете по рядам (от первого до n-го),
  где символами . (точка) обозначены свободные места, символами # (решетка) обозначены
   занятые места, а символами _ (нижнее подчеркивание) обозначен проход между креслами C и D каждого ряда.

Следующая строка содержит число m ( 1 ≤ m ≤ 100 ) – количество групп пассажиров.
 Далее в m строках содержатся описания групп пассажиров. Формат описания такой: num side position ,
  где num – количество пассажиров (число 1, 2 или 3), side – желаемая сторона самолета (строка left или right),
  position – желаемое место требовательного пассажира (строка aisle или window)."""

"""
 ABC DEF
1..._...        
2###_###
3XXX_XXX
4#X._...
"""


class OutSymbol:
    """have place symbols"""
    free_passage: str = '_'
    busy_place: str = '#'
    occupied_place: str = 'X'
    free_place: str = '.'


def pour_into_lines(n: int):
    """
    struct out
    {1:{'A':OutSymbol.occupied_place,'B':OutSymbol.busy_place,'C':OutSymbol.busy_place
    ,'_':OutSymbol.free_passage
    ,'A':OutSymbol.free_place,'B':OutSymbol.occupied_place,'C':OutSymbol.free_place}
    :paramn n count long
    :return dict place
    """
    line_dict = {'A': OutSymbol.free_place, 'B': OutSymbol.free_place, 'C': OutSymbol.free_place
        , '_': OutSymbol.free_passage
        , 'D': OutSymbol.free_place, 'E': OutSymbol.free_place, 'F': OutSymbol.free_place}
    out: dict = {}
    for i in range(1, n + 1):
        out.update({i: line_dict})
    out.items()
    return out


def roll_ticket(plane_sit: dict, temp_list: list):
    site_dict: dict = {'left': ['A', 'B', 'C'], 'right': ['D', 'E', 'F']}
    place_dict: dict = {'aisle': {'left': ['C', 'B', 'A'], 'right': ['D', 'E', 'F']},
                        'window': {'left': ['A', 'B', 'C'], 'right': ['F', 'E', 'D']}}
    count_passengers: int = int(temp_list[0])
    side: str = temp_list[1]
    position: str = temp_list[2]
    str_passenger_place: str = ''
    for row in plane_sit:
        list_pos: list = site_dict.get(side, None)
        forb_pos: str = ''
        for pos in list_pos:
            forb_pos += plane_sit.get(row, None).get(pos, None)
        if (forb_pos.count('.')) >= count_passengers:
            keys_sit = place_dict.get(position, None).get(side, None)[:count_passengers]
            temp_dict: dict = plane_sit.get(row, None).copy()
            for key in keys_sit:
                temp_dict.update({key: 'X'})
                str_passenger_place += str(row) + str(key) + ' '
            plane_sit.pop(row, None)
            plane_sit.update({row: temp_dict})
            #print(row, *plane_sit.get(row, None).values(), ' control out sit')
            #print(row + 1, *plane_sit.get(row, None).values(), ' control out sit')
            break
    print(f'passengers can take {str_passenger_place}')
    return plane_sit


def parse_passenger(n: str):
    """
    take integer for this sits
    :param n:
    :return:
    """
    plane_sit: dict = pour_into_lines(int(n))
    pair_passengers: int = int(input('Enter count pair passenger: '))
    for i in range(pair_passengers):
        query_ticket: list = input(
            'Input passengers format num side position: '
        ).split(' ')
        plane_sit = roll_ticket(plane_sit, query_ticket)
    for i in plane_sit:
        print(i, *plane_sit.get(i, None).values(), ' full')


parse_passenger(input('Enter count row in plane: '))
