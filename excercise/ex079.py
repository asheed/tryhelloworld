#!/usr/bin/env python
# -*- coding: utf8 -*

# 079 정렬
#
# 다음과 같이 문자열로 구성된 strs 리스트가 있다.
# 리스트를 문자열의 길이가 짧은 순으로 정렬하라.
#
# >>> strs = ['for', 'example', 'with', 'a', 'list']
# >>> newstrs
# ['a', 'for', 'list', 'with', 'example']

# def str_len(s):
#     return len(s)
#
# strs = ['for', 'example' 'with', 'a', 'list']
# newstrs = sorted(strs, key=str_len)
# print(newstrs)

strs = ['for', 'example', 'with', 'a', 'list']
newstrs = sorted(strs, key=lambda x : len(x))
print(newstrs)

