# TODO здесь писать код

raw_word = input("Введите слово ")
u_litr = 0
for i in raw_word:
    if raw_word.count(i) == 1:
        u_litr += 1

print("Количество уникальных букв:", u_litr)
