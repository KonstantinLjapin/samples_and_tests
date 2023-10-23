# TODO здесь писать код
import random

name_vcart = [2060, 3070, 3090]
N = int(input("Количество видеокарт: "))
list_vcart = [random.choice(name_vcart) for i in range(N)]
for i in range(N):
    print("%d Видеокарта: %d" % (i+1, list_vcart[i]))

print("Старый список видеокарт: [", *list_vcart, "]")
max_vcart = max(list_vcart)
list_vcart = [list_vcart[i] for i in range(N)
              if list_vcart[i] != max_vcart]
print("Новый список видеокарт: [", *list_vcart, "]")
