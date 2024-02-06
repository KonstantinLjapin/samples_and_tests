
from captcha.image import ImageCaptcha
from random import randint, choice
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}


def eval_binary_expr(op1, operator, op2):
    op1, op2 = int(op1), int(op2)
    return ops[operator](op1, op2)


x = 9
y = 9
random_operator: str = choice(list(ops.keys()))
print(str(x)+" ", random_operator, " "+str(y))
eval_string: str = "{}{}{}"
print(eval_string.format("9 ", "*", " 9"))
print(eval_binary_expr(*(eval_string.format(str(x)+" ", random_operator, " "+str(y)).split())))
print(eval_binary_expr(*("1 * 3".split())))
print(eval_binary_expr(*("1 ^ 3".split())))
print(eval_binary_expr(*("1 % 3".split())))
threw_integer: int = randint(1000, 9999)


def throw_captcha(temp_integer: int):
    image = ImageCaptcha(fonts=['A.ttf', 'B.ttf'])
    data = image.generate(str(temp_integer))


throw_captcha(threw_integer)


