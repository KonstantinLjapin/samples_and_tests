import functools
from typing import Callable, Any


def dec_dec(func: Any, *args, **kwargs) -> Callable:
    def wrapping(*args, **kwargs):
        def wrapper(func):
            print(func, args, kwargs, 'dec_dec')
            return func

        return wrapper
    return wrapping


@dec_dec
def dec_func(*args, **kwargs):
    @functools.wraps
    def wrapper(f):
        print(f, args, kwargs, 'dec')
        return f

    return wrapper


@dec_func('some')
def func(s: str, i: int) -> None:

    print(s, i)
    print('its work')


func('hi', 7)
