#!/usr/bin/env python
# -*- coding: utf8 -*

# 085 등급 매기기
#
# 사용자로부터 점수를 입력 받은 후 등급을 출력하라.
#
# (A: 81~100, B: 61~80: C: 41~60: D: 21~40: E: 0~20)
# 실행 예:
# score: 83
# grade is A

score = int(input('score: '))

if score >= 81 and score <= 100:
    print('grade is A')
elif score >= 61 and score <= 80:
    print('grade is B')
elif score >= 41 and score <= 60:
    print('grade is C')
elif score >= 21 and score <= 40:
    print('grade is D')
elif score >= 0 and score <= 20:
    print('grade is E')
else:
    print('입력된 점수가 유효하지 않습니다!!!')
