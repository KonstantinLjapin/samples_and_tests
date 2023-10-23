# TODO здесь писать код
raw_str = input("Введите слово: ")
if len(raw_str)%2!=0:
    raw_str = raw_str[:len(raw_str)//2] \
            + raw_str[len(raw_str) // 2+1:]
first_h = raw_str[:len(raw_str)//2]
last_h = (raw_str[len(raw_str)//2:])[::-1]
if first_h == last_h:
    print("Слово палиндром")
else:
    print("слово не палиндром")

