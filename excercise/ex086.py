#!/usr/bin/env python
# -*- coding: utf8 -*

# 086 커피 가격
#
# 커피 가격이 다음과 같을 때 이를 파이썬 딕셔너리로 구성하라.
# 사용자로부터 커피를 주문 받은 후 해당 음료에 대한 가격을 출력하라.
#
# 커피	가격
# Americano	2500
# Cafe Latte	3000
# Cappuccino	3500
# Cafe Mocha	4000
# Caramel Macchiato	4000
# Hot Chocolate	2800
# Break tea	3000

# 주문: Cafe Mocha
# 가격: 4000

coffee_prices = {}

coffee_list = ['Americano', 'Cafe Latte', 'Cappuccino', 'Cafe Mocha', 'Caramel Macchiato', 'Hot Chocolate', 'Break tea']
price_list = [2500, 3000, 3500, 4000, 4000, 2800, 3000]

coffee_prices = dict(zip(coffee_list, price_list))

order = input('주문: ')
print('가격: ', coffee_prices.get(order, '메뉴에 없는 제품입니다.'))
