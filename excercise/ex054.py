#!/usr/bin/env python
# -*- coding: utf8 -*

# 054 튜플 만들기
#
# 다음과 같은 튜플이 있을 때 이를 사용하여 t = ('A', 'b', 'c')를 만들라.
#
# >>> t = ('a', 'b', 'c')

t = ('A', 'b', 'c')

t1 = tuple(t[0].lower()) + t[1:]
# tuple(t[0].lower()) => ('a'),  t[1:] => ('b','c')
# ('a', 'b', 'c')
t = t1

print(t)