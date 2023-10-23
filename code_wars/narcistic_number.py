def narcissistic(value):
    temp: int = value
    len_val: int = len(str(value))
    un_val: int = 0
    for i in range(len_val):
        un_val += pow(temp % 10, len_val)
        temp = temp // 10
    return un_val == value


print(narcissistic(153))
