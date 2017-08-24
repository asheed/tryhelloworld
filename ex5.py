#!/usr/bin/env python
# -*- coding: utf8 -*

from urllib.request import urlopen, urlretrieve
import re
import pickle

addr = "http://www.pythonchallenge.com/pc/def/banner.p"

data = pickle.load(urlopen(addr))
print(data)

for line in data:
    print("".join([k * v for k, v in line]))
