#!/usr/bin/env python
# -*- coding: utf8 -*

# 069 딕셔너리 최솟값
#
# icecream 딕셔너리에서 최소 가격의 아이스크림 이름을 출력하라.
#
# >>> icecream = {'Tankboy': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000}

icecream = {'Tankboy': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000}

s_icecream = sorted(icecream, key=lambda x: icecream[x])

print(s_icecream[0])
