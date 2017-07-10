#!/usr/bin/env python
# -*- coding: utf8 -*

# 098 구구단 출력하기
#
# 사용자로부터 2~9 사이의 숫자를 입력 받은 후 해당 숫자에 대한 구구단을 출력하는 프로그램을 작성하라.
#
# 구구단: 3
# 3x1 = 3
# 3x2 = 6
# 3x3 = 9
# 3x4 = 12
# 3x5 = 15
# 3x6 = 18
# 3x7 = 21
# 3x8 = 24
# 3x9 = 27

dan = int(input('구구단: '))

for i in range(1,10):
    print(str(dan) + 'x' + str(i) + ' = ' + str(dan*i))