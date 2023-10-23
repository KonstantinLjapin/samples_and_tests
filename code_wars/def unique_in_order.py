def unique_in_order(sequence):
    if not sequence:
        return []
    out: list = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i-1] is not sequence[i]:
            out.append(sequence[i])
    if out[-1] is not sequence[-1]:
        out.append(sequence[len(sequence)])
    return out


print(unique_in_order([1, 2, 3, 3, -1]))
