#!/usr/bin/env python
# -*- coding: utf8 -*

# 056 튜플 수정
#
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
#
# >>> t = (1, 2, 3)
# >>> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# >>>

t = (1, 2, 3)
t[0] = 'a'

# tuple은 변경불가능한 객체 입니다.
# item assignment(=) 연산을 지원하지 않습니다.