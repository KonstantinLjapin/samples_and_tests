# TODO здесь писать код
raw_int_ch = int(input())
sum_n = 0
count_n = 0
while raw_int_ch:
    sum_n += raw_int_ch % 10
    raw_int_ch = raw_int_ch // 10
    count_n += 1

print("Сумма чисел: %d \n "
      "Количество цифр в числе: %d"
      "\nРазность суммы и кол-во: %d"
      % (sum_n, count_n, abs(sum_n-count_n)))


