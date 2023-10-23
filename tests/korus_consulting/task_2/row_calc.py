import itertools

from reader_csv import r_data


def check_data(temp_path):
    """this function check list for no digital str and mapping in int list, return list"""
    check_list = list(map(lambda x: False if x.isalpha() else int(x), r_data(temp_path)))
    check_list.remove(False)
    print(f"check row {check_list}")
    return check_list


def positive_row(task_number):
    """this function count positive number row, return number"""
    is_positive = [True if num > 0 else False for num in check_data(task_number)]
    groups = itertools.groupby(is_positive)
    occurrences_of_negatives = [len(list(g)) for k, g in groups if k]
    result = max(occurrences_of_negatives)
    print(f"max length positive row  {result}")


if __name__ == "__main__":
    pass
