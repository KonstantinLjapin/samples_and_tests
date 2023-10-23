def duplicate_encode(word):
    out: str = str()
    word = word.lower()
    for simbol in word:
        if word.count(simbol) > 1:
            out += ')'
        else:
            out += '('
    return out


print(duplicate_encode("Success))))"))
