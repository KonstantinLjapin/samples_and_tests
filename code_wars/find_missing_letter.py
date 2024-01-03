import string


def find_missing_letter(chars):
    def low_it_is(chars_un_diff):
        return chars_un_diff[0].islower()

    def find_start_later(chars_in, alphabets):
        return alphabets.index(chars_in[0])

    def roll_lists(chars_in, alphabets):
        for i in range(len(chars_in)):
            if alphabets[i + find_start_later(chars_in, alphabets)] != chars_in[i]:
                return alphabets[i + find_start_later(chars_in, alphabets)]

    if low_it_is(chars):
        alphabet = list(string.ascii_lowercase)
        return roll_lists(chars, alphabet)
    else:
        alphabet = list(string.ascii_uppercase)
        return roll_lists(chars, alphabet)


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
