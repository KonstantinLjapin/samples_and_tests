# TODO здесь писать код

import random
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


N = int(input("Введите: "))
raw_arr = [random.randint(-100, 100) for i in range(N)]

s_list = quicksort(raw_arr)

print("Изначальный список:", raw_arr)
print("Отсортированный список:", s_list)
