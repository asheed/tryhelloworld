#!/usr/bin/env python
# -*- coding: utf8 -*

S = "나는 가끔 여행을 떠나고 싶을 때가 있어"

word_list = S.split()   # word_list = ['나는', '가끔', '여행을', '떠나고', '싶을', '때가', '있어']
S = ''.join(word_list)
print(S)