import sys
from random import randint as rand_ch


def pick_up_args():
    global f_name
    global m_coordinat
    try:
        f_name = sys.argv[1]
        m_coordinat = int(sys.argv[2])
        if m_coordinat > 9801:
            #99x99=9801
            raise Exception
        if f_name != "coords.txt":
            raise Exception
    except Exception as err:
        print(err, "try: python3 helper_gen_coordinats.py coords.txt 10")
        exit()


def un_pack_coordinats(pack: list[list[int, int]]):
    out: str = str()
    for f, l in pack:
        temp: str = f'{f},{l}\n'
        out += temp
    return out


def gen_kor(coordinats_pack: list, count_coordinats) -> str:
    out: str = str()
    first_coordinat: int = rand_ch(0, 99)
    last_coordinat: int = rand_ch(0, 99)
    pair: list = [first_coordinat, last_coordinat]
    if pair not in coordinats_pack and len(coordinats_pack) < count_coordinats:
        coordinats_pack.append(pair)
        gen_kor(coordinats_pack, count_coordinats)
    return un_pack_coordinats(coordinats_pack)


def file_worker(file_name: str, max_coordinat: int) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(gen_kor([], max_coordinat))


if __name__ == "__main__":
    pick_up_args()
    file_worker(file_name=f_name, max_coordinat=m_coordinat)
