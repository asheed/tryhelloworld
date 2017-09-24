# 문제 126. 주어진 문자열(예: 'as soon as possible')에서 각 단어의 첫 글자를 취해서 하나의 단어를 만들어라.
# (split, map, join) 이용

def map_func(arg):
    return arg[0]

# s = 'as soon as possible'
s = input('문자열을 입력하세요 : ')

print(''.join(map(map_func, s.split())))
# print(''.join(map(lambda arg:arg[0], s.split())))