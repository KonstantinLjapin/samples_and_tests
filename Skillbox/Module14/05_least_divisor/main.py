# TODO здесь писать код

def nod_m(n):
    i = 2
    while n % i != 0:
        i += 1
    print("Наименьший делитель, отличный от единицы:", i)


nod_m(int(input("Введите число: ")))
