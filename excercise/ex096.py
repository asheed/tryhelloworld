#!/usr/bin/env python
# -*- coding: utf8 -*

# 096 애완 동물 출력하기
#
# 다음과 같이 애완 동물 리스트가 있을 때 애완 동물의 이름과 애완 동물의 글자수를 출력하라.
#
# >>> pet = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']
# 실행 예:
# dog 3
# cat 3
# parrot 6
# squirrel 8
# goldfish 8

pet = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']

for item in pet:
    print(item, len(item))