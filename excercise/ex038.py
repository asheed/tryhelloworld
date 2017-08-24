#!/usr/bin/env python
# -*- coding: utf8 -*

# 038 문자열 분리 및 합치기
#
# 'spam egg' 문자열을 'egg spam'으로 변경하라.

orig = 'spam egg'

orig_temp = orig.split(' ')

orig_temp.reverse()
# ['egg','spam'] ==> 'egg spam'
print(' '.join(orig_temp))
