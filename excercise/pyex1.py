# 문1. 아래와 같은 문자열에서 사용된 단어를 알파벳 순서대로 출력하세요.(중복허용)
# 실행 예
# Python
# We
# a
# an
# and
# and
# by
# creating
# development
# environment
# existing
# focus
# for
# in
# it
# it
# language
# making
# materials
# new
# on
# possible
# programming
# propose
# scripting
# start
# teach
# teaching
# to
# to
# to

s = '''We propose to start by making it possible to teach programming in Python,
an existing scripting language, and to focus on creating a new development
environment and teaching materials for it.'''

word_list = s.replace(',', '').replace('.','').split()
word_list.sort()

for word in word_list:
    print(word)