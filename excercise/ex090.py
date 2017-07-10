#!/usr/bin/env python
# -*- coding: utf8 -*

# 090 대문자 소문자 변환
#
# 파이썬 문자열에는 isupper()와 islower()라는 메서드가 존재한다.
#
# >>> 'KOREA'.isupper()
# True
# >>> 'korea'.islower()
# True
# 사용자로부터 문자열을 입력 받은 후 대문자는 소문자로 소문자는 대문자로 출력하는 프로그램을 작성하라.
#
# 입력: PYTHON
# python

user_input = input('입력: ')

if user_input.isupper():
    print(user_input.lower())
elif user_input.islower():
    print(user_input.upper())

