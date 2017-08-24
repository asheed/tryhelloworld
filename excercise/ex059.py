#!/usr/bin/env python
# -*- coding: utf8 -*

# 059 튜플을 이용한 swap
#
# 다음 코드를 실행해보고 최종적으로 a와 b가 바인딩하는 값을 설명하라.
#
# >>> a = 10
# >>> b = 20
# >>> a, b = b, a
# >>>

# temp = 0
a = 10
b = 20

# a = b   # a 20
# b = a   # b 20

# temp = a    # temp 10
# a = b       # a 20
# b = temp    # b 10

(a, b) = (b, a)

print('a is', a)
print('b is', b)