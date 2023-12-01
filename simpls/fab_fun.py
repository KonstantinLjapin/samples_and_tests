general = 0
first_var = '5'
action = '*'
last_var = '4'

operators = {
    '+':lambda a, b: a + b,
    '-':lambda a, b: a - b,
    '*':lambda a, b: a * b,
    '/':lambda a, b: a / b,
}
general += operators[action](int(first_var), int(last_var))
print(general)
