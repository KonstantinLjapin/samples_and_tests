
def roma_arabic(rome_str: str) -> int:
    """function take string, checking exception or trans too arabic"""
    exception_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    rome_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    out = 0
    while rome_str:
        if len(rome_str) > 1 and rome_str[0] + rome_str[1] in exception_dict.keys():
            out += exception_dict.get(rome_str[0] + rome_str[1])
            rome_str = rome_str[2:]
        else:
            out += rome_dict.get(rome_str[0])
            rome_str = rome_str[1:]
    return out


if __name__ == "__main__":
    print(roma_arabic("MCCXXXIV"))
