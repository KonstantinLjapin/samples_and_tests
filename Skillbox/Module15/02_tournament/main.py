# TODO здесь писать код
i = "Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар"
name_list = i.split(', ')
name_list = [name_list[i] for i in range(8) if i % 2 == 0]
print(name_list)
