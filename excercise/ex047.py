#!/usr/bin/env python
# -*- coding: utf8 -*

# 047 평균값 계산
#
# 다음은 대신증권의 최근 5일 종가 데이터이다. 최근 5일치 종가의 평균 값을 출력하라.
#
# close_price_daeshin = [10000, 10500, 10300, 10700, 11100]
# 실행 예:
# average:  10520.0

close_price_daeshin = [10000, 10500, 10300, 10700, 11100]

import math

average = sum(close_price_daeshin) / len(close_price_daeshin)

print("average: {}".format(average))
