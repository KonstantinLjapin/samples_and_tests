import re
with open('for_parce_properties.txt', 'r') as f:
    some_parce = f.read()
    with open('out_parce.txt', 'w+') as s:
        temp = some_parce
        key = "gaiaId"
        gaiaId = ''.join(re.findall(r'\d+', (temp[temp.find(key):])[:temp.find(",")]))
        s.write(str(temp))
        print(gaiaId)
        print(type(some_parce))
