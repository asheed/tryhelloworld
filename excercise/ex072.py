#!/usr/bin/env python
# -*- coding: utf8 -*

# 072 List comprehension
#
# List comprehension을 사용하여 nums 리스트에 있는 값에 대해 홀수와 짝수로 구성된 리스트를 생성하고 이를 출력하라.
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# even: [2, 4, 6, 8, 10]
# odd:  [1, 3, 5, 7, 9]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [i for i in nums if i % 2 == 0]
odd = [i for i in nums if i % 2 != 0]

print('even:', even)
print('odd:', odd)