#!/usr/bin/env python
# -*- coding: utf8 -*

# 073 List comprehension
#
# files 리스트에 다음과 같은 데이터가 있을 때 이 중 확장자가 *.txt 파일만 리스트로 구성하고 이를 출력하라.
#
# files = ['a.txt', 'b.txt', 'exer.avi', 'sing.mp3', 'ultra.avi']
# 실행 예:
# ['a.txt', 'b.txt']

files = ['a.txt', 'b.txt', 'exer.avi', 'sing.mp3', 'ultra.avi']

l = [s for s in files if s.split('.')[-1] == 'txt']

print(l)