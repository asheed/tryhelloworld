#!/usr/bin/env python
# -*- coding: utf8 -*

# 064 딕셔너리 수정
#
# 062에서 만든 딕셔너리에서 메로나(Melona)의 가격을 1300으로 수정하라.

icecream_list = {'Melona': 1000, 'Pollapo': 1200, 'Ppangppare': 1800, 'Tankboy': 1200, 'Heathunting': 1200, 'Worldcone': 1500}

icecream_list['Melona'] = 1300

print('메로나 가격: ', icecream_list['Melona'])