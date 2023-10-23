def biggest_dict(some):
    my_dict: dict
    for i in some:
        my_dict.update({i:i})
    return my_dict