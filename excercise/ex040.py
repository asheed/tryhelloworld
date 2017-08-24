#!/usr/bin/env python
# -*- coding: utf8 -*

# 040 문자열 분리
#
# 사용자로부터 '10:00:01'와 같은 형태로 시간을 입력 받은 후
# 해당 시간이 00:00:00 으로부터 몇 초가 지났는지를 출력하라.
#
# time: 10:00:01
# 36001

user_time = input("time: ")
# "10:00:01"

time_list = user_time.split(':')
# list -> ['10', '00', '01']

total_seconds = 0

total_seconds = int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])

print(total_seconds)
