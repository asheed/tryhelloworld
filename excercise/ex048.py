#!/usr/bin/env python
# -*- coding: utf8 -*

# 048 리스트 형 변환
#
# 다음 리스트를 튜플로 변경하라.
#
# >>> data = ['a', 'b', 'c', 'd', 'e']
# 실행 예:
# >>> type(data)
# <class 'tuple'>
# >>> data
# ('a', 'b', 'c', 'd', 'e')
# >>>

data = ['a', 'b', 'c', 'd', 'e']
print(data)
print(type(data))

data = tuple(data)

print(data)
print(type(data))
