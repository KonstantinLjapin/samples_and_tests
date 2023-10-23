# TODO здесь писать код
import random
N = int(input("Введите кол-во: "))
el_list = [random.randint(-10, N) for i in range(N)]
K = int(input("Сдвиг: "))
lst = el_list
for i in range(K):
    lst = lst[1:] + lst[:1]

print("Изначальный список:", el_list)
print("Сдвинутый список:", lst)
