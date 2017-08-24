#!/usr/bin/env python
# -*- coding: utf8 -*

from urllib.request import urlopen, urlretrieve
import re, zipfile

uri = "http://www.pythonchallenge.com/pc/def/channel.zip"
urlretrieve(uri, 'channel.zip')
f = zipfile.ZipFile('channel.zip')
num = '90052'
comments = []
# 정규표현식 패턴 생성
# 그룹을 사용하여 숫자만 추출하여 num에 다시 사용
pattern = re.compile("Next nothing is (\d+)")

while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)

print(comments)
print("".join(comments))