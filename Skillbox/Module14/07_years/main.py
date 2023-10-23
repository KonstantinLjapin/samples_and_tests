# TODO здесь писать код

a, b = int(input("Введите первый год: ")), int(input("Введите второй год: "))
print("Годы от %d до %d с "
      "тремя одинаковыми цифрами:" % (a, b))
if a > b:
    a, b = b, a
for x in range(a, b + 1):
    m = str(x)
    if m.count(m[0]) == 3 or m.count(m[1]) == 3:
        print(x)
