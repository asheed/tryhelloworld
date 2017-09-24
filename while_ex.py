# selected = None
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요>')
#     # print(selected)
#
# print('선택된 값은', selected)

# patterns = ['가위', '보', '보']
#
# for pattern in patterns:
#     print(pattern)
#
# for i in range(len(patterns)):
#     print(patterns[i])
#
# i = 0
# while i < len(patterns):
#     print(patterns[i])
#     i = i + 1

# sizes = [33, 35, 34, 37, 32, 35, 39, 32, 35, 29]
# for i, size in enumerate(sizes):
#     if size == 32:
#         print("사이즈 32인 바지는 {}번째에 있다".format(i+1))
#         break

numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌수 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a, b, a/b))