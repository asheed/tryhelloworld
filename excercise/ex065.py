#!/usr/bin/env python
# -*- coding: utf8 -*

# 065 딕셔너리와 리스트
#
# 다음 표를 딕셔너리로 구성하라. 아이스크림의 이름은 딕셔너리의 'key'이고 희망 가격과 남은 수량은 리스트로 구성한 후 딕셔너리의 'value'로 사용하라.
#
# 이름	희망 가격	남은 수량
# Melona	1000	10
# Pollapo	1200	7
# Ppangppare	1800	6
# Tankboy	1200	5
# Heathunting	1200	4
# Worldcorn	1500	3

icecream_list = {
    '메로나': [1000, 10],
    '폴라포': [1200, 7],
    '빵빠레': [1800, 6],
    '탱크보이': [1200, 5],
    '더위사냥': [1200, 4],
    '월드콘': [1500, 3]
}

print(icecream_list['메로나'])