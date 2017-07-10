#!/usr/bin/env python
# -*- coding: utf8 -*

# 055 zip과 튜플
#
# 다음 코드의 실행 결과를 보고 zip 함수의 역할을 설명하라.
#
# >>> t = ['a', 'b', 'c']
# >>> n = [1, 2, 3]
# >>> list(zip(t, n))
# [('a', 1), ('b', 2), ('c', 3)]
# >>>

t = ['a', 'b', 'c']
n = [1, 2, 3]
z = list(zip(t, n))
print(z)

s1 = "nice"
s2 = "good"
z1 = list(zip(s1, s2))

print(z1)

# 두개의 iterable 데이터를 묶어 튜플 리스트를 생성합니다.
