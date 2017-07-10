#!/usr/bin/env python
# -*- coding: utf8 -*

# 075 Star expression
#
# 다음은 S전자의 최근 6분기의 영업이익이다.
# 가장 최근 분기의 영업이익을 나머지 5분기 영업이익을 비교하라.
# sales_profit 리스트에서 우측 끝이 가장 최근 분기의 영업이익이다.
#
# sales_profit = [5.98, 6.90, 7.39, 6.14, 6.68, 8.10]
# 실행 예:
# ratio(current/before) = 1.22

sales_profit = [5.98, 6.90, 7.39, 6.14, 6.68, 8.10]
*_, before, current = sales_profit

print('ratio(current/before) = ', round(current / before, 2))