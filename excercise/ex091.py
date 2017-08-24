#!/usr/bin/env python
# -*- coding: utf8 -*

# 091 역방향 순환
#
# 다음 리스트에 있는 숫자를 역 방향으로 출력하라.
#
# >>> nums = [1, 2, 3, 4, 5]
# 실행 예:
# 5
# 4
# 3
# 2
# 1

nums = [1, 2, 3, 4, 5]

# nums.reverse()
#
# for i in nums:
#     print(i)

for i in sorted(nums, reverse=True):
    print(i)