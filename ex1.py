#!/usr/bin/env python
# -*- coding: utf8 -*

s = "map"
result = ''
intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'

trantab = str.maketrans(intab, outtab)

result = s.translate(trantab)
# for i in s:
#     if not i.isalpha():
#         result += i
#     elif i.isalpha():
#         result += chr(ord(i) + 2)

print(result)