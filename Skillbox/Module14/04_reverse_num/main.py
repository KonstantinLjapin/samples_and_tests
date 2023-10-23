# TODO здесь писать код

def tr_str(n): return float(((n[:n.find('.')])[::-1]) + '.' + ((n[n.find('.') + 1:])[::-1]))


turn_first = tr_str(str(input("Введите первое число:")))
turn_last = tr_str(str(input("Введите второе число: ")))
print("Первое число наоборот: %.2f"
      "\nВторое число наоборот: %.2f"
      "\nСумма: %.2f" % (turn_first, turn_last, turn_last+turn_first))
