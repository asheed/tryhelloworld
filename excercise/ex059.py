#!/usr/bin/env python
# -*- coding: utf8 -*

# 059 튜플을 이용한 swap
#
# 다음 코드를 실행해보고 최종적으로 a와 b가 바인딩하는 값을 설명하라.
#
# >>> a = 10
# >>> b= 20
# >>> a, b = b, a
# >>>

a = 10
b = 20
a, b = b, a

print('a is', a)
print('b is', b)