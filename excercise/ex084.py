#!/usr/bin/env python
# -*- coding: utf8 -*

# 084 큰수 찾기
#
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
#
# 실행 예:
# input number1: 10
# input number2: 9
# input number3: 20
# 20

num1 = int(input('input number1: '))
num2 = int(input('input number2: '))
num3 = int(input('input number3: '))

num = [num1, num2, num3]

print(max(num))
