#!/usr/bin/env python
# -*- coding: utf8 -*

# 100 문자열 뒤집기
#
# 사용자로부터 문자열을 입력받은 후 입력 문자열을 뒤집어 출력하는 프로그램을 작성할.
#
# 실행 예:
# 문자열 입력: python world
# dlrow nohtyp

s = input('문자열 입력: ')

# l = -len(s)
# i = -1
# while i >= l:
#     print(s[i], end='')
#     i -= 1

rev_s = ''

for i in s:
    rev_s = i + rev_s

print(rev_s)