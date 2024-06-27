import sys
import math


def pick_up_args():
    global f_name
    global radius
    try:
        f_name = sys.argv[1]
        radius = int(sys.argv[2])
        if radius > 50:
            #99\2~=50
            raise Exception
        if f_name != "coords.txt":
            raise Exception
    except Exception as err:
        print(err, "try: python3 nuke.py coords.txt 10")
        exit()


def checkin_points(file) -> list[[int, int]]:
    pack: list = []
    for line in file:
        temp: list = line.split(',')
        try:
            first: int = int(temp[0])
            last: int = int(temp[1])
            if first >= 99 and not 0 <= first or last >= 99 and not 0 <= last:
                raise Exception
            pack.append([first, last])
        except Exception as err:
            print(err, "Coordinate error")
    return pack


def max_point_in_radius(pack: list[[int, int]], r: int):
    max_points_in_radius: dict = {}
    for x, y in pack:
        count_points: int = 0
        for xk, yk in pack:
            if (x - xk) ** 2 / r ** 2 + (y - yk) ** 2 / r ** 2 < 1:
                count_points += 1
        max_points_in_radius.update({count_points: [x, y]})
    return (f"max_points {max(max_points_in_radius.keys())} : "
            f" {max_points_in_radius.get(max(max_points_in_radius.keys()), '1')}")


def file_worker(file_name: str, r: int) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        pack: list[[int, int]] = checkin_points(file)
        print(max_point_in_radius(pack, r))


if __name__ == "__main__":
    pick_up_args()
    file_worker(file_name=f_name, r=radius)
