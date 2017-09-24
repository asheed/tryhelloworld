# 문제 10-5. 주어진 문자열(예: 'as soon as possible')에서 각 단어의 첫 글자를 취해서 하나의 단어를 만들어라.
# (split, map, join) 이용

s = 'as soon as possible'
print(''.join(map(lambda x:x[0], s.split())))