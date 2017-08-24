#!/usr/bin/env python
# -*- coding: utf8 -*

# 077 Set 자료구조
#
# items가 다음과 같은 리스트일 때 중복 아이템이 제거된 리스트를 생성하라. (힌트: set 사용)
#
# >>> items = [1, 6, 2, 3, 4, 4, 6, 6, 7, 2, 7]
# >>>
# 실행 예:
# >>> new_items
# [1, 2, 3, 4, 6, 7]
# >>>

items = [1, 6, 2, 3, 4, 4, 6, 6, 7, 2, 7]

new_items = set(items)

print(new_items)

item = [6,7,8,9]
item = set(item)
print(item)
plus_set = new_items.intersection(item)
print(plus_set)