# patterns = \
#     ['가위', '보', '보', '가위', '가위', '가위', '보', '가위', '바위', '보']
#
# for i in patterns:
#         print(i)

names = ['철수', '영희', '바둑이', '귀도']
#          0      1       2       3

for i in range(4):
    print('{} 번 : {}'.format(i, names[i]))

print('='*50)

for i, data in enumerate(names):
    # 0, '철수'
    # 1, '영희'
    # 2, '바둑이'
    # 3, '귀도'
    print('{} 번 : {}'.format(i, data))

for i in range(1, 100):
    address = 'http://naver.com/?search=abc&data='
    query = address + str(i)


alpha = []
for i in range(97, 97 + 26):
    alpha.append(chr(i))

print(alpha)
str_alpha = ''.join(alpha)

print(str_alpha)
