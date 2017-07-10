#!/usr/bin/env python
# -*- coding: utf8 -*

# 068 딕셔너리 values
#
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
#
# >>> icecream = {'Tankboy': 1200, 'Pollapo': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000, 'Heathunting': 1200}

icecream = {'Tankboy': 1200, 'Pollapo': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000, 'Heathunting': 1200}

value_list = icecream.values()

print(list(value_list))
