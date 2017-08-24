def camelToPothole(s):
    retStr = ''
    for i, cur_char in enumerate(s):
        if i >= 1 and s[i-1].islower() and cur_char.isupper():
            retStr += '_' + cur_char.lower()
        elif i >= 1 and cur_char.isnumeric():
            retStr += '_' + cur_char
        else:
            retStr += cur_char
    return retStr
import re

#camelToPothole = lambda src: re.sub("([A-Z0-9])", lambda m:"_"+m.group().lower(), src)

print(camelToPothole('numGoat30'))
print(camelToPothole('codingDojang'))
print(camelToPothole('123testAbc'))
print(camelToPothole('GoodBoy'))

def do(l):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(["_" + c.lower() if c in a else c for c in l])

print(do('numGoat30'))
print(do('123testAbc'))