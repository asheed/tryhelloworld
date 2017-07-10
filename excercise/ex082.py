#!/usr/bin/env python
# -*- coding: utf8 -*

# 082 큰수 찾기
#
# 사용자로부터 두 개의 숫자를 입력 받은 후 큰 숫자를 화면에 출력하라.
#
# 실행 예:
#
# num1:10
# num2:7
# 10

# case1: list와 max 함수 사용
# num = []
# num.append(int(input('num1:')))
# num.append(int(input('num2:')))

# print(max(num))

# case2: if문 사용
num1 = int(input('num1:'))
num2 = int(input('num2:'))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('두수는 같습니다.', num1)