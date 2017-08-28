#!/usr/bin/env python
# -*- coding: utf8 -*

# http://www.pythonchallenge.com/pc/return/5808.html
from PIL import Image
# from urllib.request import urlretrieve
import time, re

# uri = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
# urlretrieve(uri, 'cave.jpg')
#
# time.sleep(1)

img = Image.open("cave.jpg")
(w, h) = img.size
print("="*50)
print("그림정보")
print("가로길이 : {}, 세로길이 : {}".format(w, h))
print("getpixel 함수를 사용하여 (0,0)의 정보 가져오기")

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = img.getpixel((i, j))
        if (i + j) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

even.save('even.jpg')
odd.save('odd.jpg')