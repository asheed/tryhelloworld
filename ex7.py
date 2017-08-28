#!/usr/bin/env python
# -*- coding: utf8 -*

# http://www.pythonchallenge.com/pc/def/oxygen.html
from PIL import Image
from urllib.request import urlretrieve
import time, re

uri = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
urlretrieve(uri, 'oxygen.png')

time.sleep(1)

img = Image.open("oxygen.png")
print("="*50)
print("그림정보")
print("가로길이 : {}, 세로길이 : {}".format(img.width, img.height))
print("getpixel 함수를 사용하여 (0,0)의 정보 가져오기")
print("img.getpixel((0,0)) : {}", img.getpixel((0, 0)))

# 그림의 중간부분이 이상하다.
# 가운데에 위치한 픽셀정보를 가져온다.
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
print(row)
# 출력해보니 7개씩 반복되어 중복을 줄여서 뽑아낸다.
row = row[::7]
print(row)
# 그림의 가운데 부분은 그레이 스케일임을 알수 있다.
# r == g == b 이면 그레이 스케일이므로 아래와 같이 그 부분만 빼낸다.
ords = [r for r, g, b, a in row if r == g == b]
print(ords)
nums = re.findall("\d+", "".join(map(chr, map(int, ords))))

print(nums)

result = "".join(map(chr, map(int, nums)))

print(result)