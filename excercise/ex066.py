#!/usr/bin/env python
# -*- coding: utf8 -*

# 066 딕셔너리 인덱싱
#
# 다음 코드에서 에러가 발생한 원인을 설명하라.
#
# >>> icecream = {
#        'Tankboy': 1200,
#        'Pollapo': 1200,
#        'Ppangppare': 1800,
#        'Worldcorn': 1500,
#        'Melona': 1000,
#        'Heathunting': 1200
# }
# >>> icecream['Nugaba']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['Nugaba']
# KeyError: 'Nugaba'
# >>>

icecream = {'Tankboy': 1200, 'Pollapo': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000, 'Heathunting': 1200}

print(icecream.get('Tankboy', '그런 아이스크림은 존재하지 않습니다.'))

# 에러명이 KeyError 즉, 존재하지 않는 키에 접근하려고 했을때 발생

