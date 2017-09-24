#!/usr/bin/env python
# -*- coding: utf8 -*

S = "나는 가끔 여행을 떠나고 싶을 때가 있어"

word_list = S.split()   # word_list = ['나는', '가끔', '여행을', '떠나고', '싶을', '때가', '있어']
word_list.reverse()     # word_list = ['있어', '때가', '싶을', '떠나고', '여행을', '가끔', '나는']

# l = []
# for x in range(1,10):
#     l.append(x**2)
#
# print(l)
#
# l1 = [x**2 for x in range(1,10)] # list comprehension
#
# print(l1)

S = ' '.join([x[::-1] for x in word_list])
#['어있','가때','을싶','고나떠','을행여','끔가','는나']
print(S)
