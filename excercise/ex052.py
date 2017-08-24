#!/usr/bin/env python
# -*- coding: utf8 -*

# 052 리스트 변환
#
# 다음 튜플을 리스트로 변환하라.
#
# interest = ('삼성전자', 'LG전자', 'SK Hynix')

interest = ('삼성전자', 'LG전자', 'SK Hynix')

print(interest)
print('원래 interest의 타입 : ' + str(type(interest)))

interest = list(interest)

print(interest)
print('변환 후 interest의 타입 : ' + str(type(interest)))

interest = tuple(interest)