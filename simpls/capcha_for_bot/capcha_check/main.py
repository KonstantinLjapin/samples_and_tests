import datetime
import time
from typing import Any
from captcha.image import ImageCaptcha
from random import randint
import asyncio
from time import monotonic
threw_integer: int = randint(1000, 9999)


def waiter_time(delay):
    time.sleep(delay)
    return True


def throw_captcha(temp_integer: int):
    image = ImageCaptcha(fonts=['A.ttf', 'B.ttf'])
    data = image.generate(str(temp_integer))


throw_captcha(64535)
