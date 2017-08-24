#!/usr/bin/env python
# -*- coding: utf8 -*

# 097 3의 배수 출력하기
#
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.
#
# 실행 예:
# 3 6 9 12 15 18 21 24 27 30

for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=' ')

# l = [i for i in range(1, 31) if i % 3 == 0]
# print(l)
