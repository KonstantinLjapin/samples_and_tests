my_dict: dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(kwargs)


def to_dict(*args):
    for i in args:
        yield {i: i}


for i in to_dict(1,2,3):
    print(i)
