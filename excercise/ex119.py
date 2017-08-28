#!/usr/bin/env python
# -*- coding: utf8 -*

S = "나는 가끔 여행을 떠나고 싶을 때가 있어"

word_list = S.split()   # word_list = ['나는', '가끔', '여행을', '떠나고', '싶을', '때가', '있어']
word_list.reverse()     # word_list = ['있어', '때가', '싶을', '떠나고', '여행을', '가끔', '나는']
S = ' '.join([lambda x:x[::-1] for x in word_list])
print(S)