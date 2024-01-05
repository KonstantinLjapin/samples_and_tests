def find_outlier(integers: list) -> int:
    even: list = []
    odd: list = []
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        if len(even) > 1 and len(odd) > 0 or len(even) > 0 and len(odd) > 1:
            if len(even) == 1:
                return even[0]
            else:
                return odd[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))

