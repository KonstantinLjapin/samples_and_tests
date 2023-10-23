# TODO здесь писать код
import random

N = int(input("Введите N: "))
cels_list = [random.randint(0, N) for i in range(N)]
for i in range(N):
    print("Эффективность %d клетки: %d" % (i+1, cels_list[i]))

print("", *[cels_list[i] for i in range(N) if i > cels_list[i]])
