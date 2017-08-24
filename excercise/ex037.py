#!/usr/bin/env python
# -*- coding: utf8 -*

# 037 경로 분리
#
# 사용자로부터 윈도우 디렉터리 경로를 입력 받은 후 가장 최종 디렉터리를 출력하라.
#
# 실행 예:
# 경로: c:\program files\python
# python

path = input("경로: ")
last_dir = path.split('\\')[-1]
print(last_dir)