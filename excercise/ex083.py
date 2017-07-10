#!/usr/bin/env python
# -*- coding: utf8 -*

# 083 홀수 짝수 출력하기
#
# 사용자로부터 입력 받은 숫자가 홀수인지 짝수인지 출력하라.
#
# 실행 예:
# input number: 4
# even number

number = int(input('input number: '))
if number % 2 == 0: # 짝수
    print('even number')
else:
    print('odd number')