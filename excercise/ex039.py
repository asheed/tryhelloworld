#!/usr/bin/env python
# -*- coding: utf8 -*

# 039 문자열 개수 확인
#
# 'Python python pYthon java Java'에서 대소문자를 구분하지 않고 사용된 python 문자열의 개수를 출력하라.

s = 'Python python pYthon java Java'
print(s.lower().count('python'))

