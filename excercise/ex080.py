#!/usr/bin/env python
# -*- coding: utf8 -*

# 080 리스트와 range
#
# range() 함수를 사용하여 0~9까지의 원소를 갖는 리스트를 생성하라.
#
# 실행 예:
# >>> nums
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>>

nums = [i for i in range(10)]
print(nums)

nums1 = list(range(10))
print(nums1)