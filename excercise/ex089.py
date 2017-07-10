#!/usr/bin/env python
# -*- coding: utf8 -*

# 089 칼로리 계산기
#
# 계단 한 칸당 0.11 칼로리를 한 걸음당 0.033 칼로리가 소비된다.
# 사용자로부터 오늘 오른 총 계단의 수와 총 걸음수를 입력 받은 후 당일 소비 칼로리를 출력하라.
#
# 실행 예:
#
# 입력: 97 계단 9700 보
# 당일 소비 칼로리: 330.77

user_input = input('입력: ')
input_list = user_input.split(' ')
steps = int(input_list[0])
walks = int(input_list[2])

print('당일 소비 칼로리: ', round(steps * 0.11 + walks * 0.033, 2))

