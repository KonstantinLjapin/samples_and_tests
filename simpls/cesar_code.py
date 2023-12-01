
def cesar_code(in_str):
    shift = 1
    out_str = str()
    for i in in_str:
        if i == "\n":
            shift += 1
        if i.isalpha():
            out_str += chr((ord(i) + shift) % ord('z'))
        else:
            out_str += i
    return out_str


print(cesar_code("Hello\nHello\nHello\nHello"))
