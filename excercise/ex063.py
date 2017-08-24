#!/usr/bin/env python
# -*- coding: utf8 -*

# 063 딕셔너리 인덱싱
#
# 062에서 만든 딕셔너리를 사용하여 메로나(Melona) 가격을 출력하라.
#
# 실행 예:
# 메로나 가격:  1000

icecream_list = {
                 'Melona': 1000,
                 'Pollapo': 1200,
                 'Ppangppare': 1800,
                 'Tankboy': 1200,
                 'Heathunting': 1200,
                 'Worldcone': 1500
}

print('메로나 가격: ', icecream_list['Melona'])

print('메로나 가격(get함수를 사용) : ', icecream_list.get('Melona'))
