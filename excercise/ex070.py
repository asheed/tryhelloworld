#!/usr/bin/env python
# -*- coding: utf8 -*

# 070 딕셔너리 update
#
# contact1과 contact2 딕셔너리가 있을 때 두 개의 딕셔너리의 key-value 쌍을 모두 포함하는 contact 딕셔너리를 생성하라. (힌트: 딕셔너리 update 메서드 사용)
#
# >>> contact1 = {'chusu': '010-3111-2393', 'minsu':'010-3112-9932'}
# >>> contact2 = {'jaein': '011-1312-2121', 'jongho':'010-8821-1311'}
# 실행 예:
# >>> contact
# {'jongho': '010-8821-1311', 'chusu': '010-3111-2393', 'jaein': '011-1312-2121', 'minsu': '010-3112-9932'}
# >>>

contact1 = {'chusu': '010-3111-2393', 'minsu':'010-3112-9932'}
contact2 = {'jaein': '011-1312-2121', 'jongho':'010-8821-1311'}

contact = {}
contact1.update(contact2)

print(contact1)