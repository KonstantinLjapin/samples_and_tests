def sum_two_smallest_numbers(numbers: list):
    if numbers:
        numbers.sort()
        min_first = numbers[0]
        min_next = numbers[1]
        out = min_first + min_next
        return out
