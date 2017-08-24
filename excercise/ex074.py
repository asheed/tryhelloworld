#!/usr/bin/env python
# -*- coding: utf8 -*

# 074 Star expression
#
# 파이썬3에 추가된 star expression은 다음과 같이 데이터를 언패킹하는데 유용하게 사용할 수 있다.
#
# >>> a, b, *c = [0,1,2,3,4]
# >>> a
# 0
# >>> b
# 1
# >>> c
# [2,3,4]
# >>>
# 다음은 동계올림픽에서 조아름 선수가 받은 10개의 수영 점수이다.
# 하지만 최근 두 경기는 부정 출발로 인해 점수를 인정받지 못하게 되었다.
# 조아름 선수가 공식적으로 인정받은 8개의 수영 성적에 대한 평균값을 start expression을 사용하여 구현하라.
# 점수는 score 리스트에 좌측에서 우측으로 기록되었으며, 최근 점수가 우측끝에 저장되어 있다.
#
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

scores.reverse()
print(scores)
# _, _, *new_score =
_, _, *new_score = scores
# _ = 9.4
# _ = 7.8
# new_score = [9.5, 9.9, 9.7, 9.3, 9.2, 8.7, 8.9, 8.8]
print(len(new_score))
print('조아름 선수의 최근 8경기 평균 점수:', sum(new_score) / len(new_score))
# print('조아름 선수의 최근 8경기 평균 점수:', sum(scores[:8]) / (len(scores)-2))