#!/usr/bin/env python
# -*- coding: utf8 -*

from urllib.request import urlopen
import re
# import urllib.parse as parse
# addr = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
# values = {
#     'nothing': 44827
# }
# params = parse.urlencode(values)
# url = addr + "?" + params
# html = urlopen(url)
#
# while html.status == 200:
#     data = html.read().decode()
#     print(data)
#     values['nothing'] = data.split()[-1]
#     params = parse.urlencode(values)
#     url = addr + "?" + params
#     html = urlopen(url)

addr = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

#num = "12345"  # 처음에는 이걸로 시작
num = str(16044/2)      # 한번 종료 이후 2로 나눈값으로 다시 시작

# 정규표현식 패턴 생성
# 그룹을 사용하여 숫자만 추출하여 num에 다시 사용
pattern = re.compile("and the next nothing is (\d+)")

while True:
    content = urlopen(addr % num).read().decode("utf-8")
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)