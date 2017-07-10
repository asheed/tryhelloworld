#!/usr/bin/env python
# -*- coding: utf8 -*

# 088 환율 계산기
#
# 087 문제를 if, elif, else와 같은 제어문을 사용하지 않고 풀어라.
# (힌트: 딕셔너리를 사용하여 통화별 매매 금액 산출)

convert_list = {
    '달러': 1167,
    '엔': 1.096,
    '유로': 1268,
    '위안': 171
}

user_input = input('입력: ')
money = int(user_input.split(' ')[0])
currency = user_input.split(' ')[1]

print(int(money * convert_list[currency]), ' 원')
