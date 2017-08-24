# for i in range(11172):
#     if i % 10 == 0:
#         print()
#     print(chr(44032 + i), end='')

# for ... in, range, enumerate
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print('='*30)
print('range를 사용')
for i in range(1, 13):
    print('{}월의 날짜 수는 {}일 입니다.'.format(i, days[i-1]))


print('='*30)
print('enumerate를 사용')
for i, day in enumerate(days):
    print('{}월의 날짜 수는 {}일 입니다.'.format(i+1, day))

# i = 0, day = 31
# i = 1, day = 29
# i = 2, day = 31
...
# i = 11, day = 31