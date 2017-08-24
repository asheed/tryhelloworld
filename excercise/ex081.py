#!/usr/bin/env python
# -*- coding: utf8 -*

# 081 if else 문
#
# 파일 이름이 리스트에 저장되어 있을 때 확장자가 *.h나 *.c인 파일에 대한 리스트를 생성하라.
# (힌트: list comprehension, string endswith 메서드)
#
# filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']
# 실행 예:
# >>> result
# ['intra.h', 'intra.c']

filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

result = [filename for filename in filenames if filename.endswith(('.h', '.c'))]

nums = [i for i in range(10) if i % 2 == 0]

print(result)
print(nums)