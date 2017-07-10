#!/usr/bin/env python
# -*- coding: utf8 -*

# 076 List sorting과 slicing
#
# nums 리스트에 다음과 같은 데이터가 있을 때 가장 큰 3개의 아이템과 가장 작은 3개의 아이템을 출력하라.
#
# nums = [-1, 10, 2, 8, 9, 7, -11, 20, 21, 37, 56, 21, -27]
# 실행 예:
# largest: [21, 37, 56]
# smallest: [-27, -11, -1]

nums = [-1, 10, 2, 8, 9, 7, -11, 20, 21, 37, 56, 21, -27]
sorted_nums = sorted(nums)

print('largest: ', sorted_nums[-3:])
print('smallest: ', sorted_nums[0:3])