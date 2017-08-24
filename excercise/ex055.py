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

z = dict(zip(t, n))
print(z)

s1 = "nice"
s2 = "good"
z1 = list(zip(s1, s2))

print(z1)

x = range(1, 11)
# [1,2,3,4,5,6,7,8,9,10]
y = range(1, 11)
# [1,2,3,4,5,6,7,8,9,10]
x = ['김머시기', '홍길동']
y = [90, 100]
z = [100, 20]
points = dict(zip(x, y))
print(points)

# 두 개의 iterable 데이터를 묶어 쌍으로 리스트 또는 사전을 생성합니다.
