# TODO здесь писать код
def m_finder_coin(x, y, r):
    if (x ** 2 + y ** 2) ** 0.5 <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


m_finder_coin(float(input("X: ")), float(input("Y: ")), float(input("Введите радиус: ")))
