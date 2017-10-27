rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다.'.format(first_color))


last_color = rainbow[-1]
print('무지개의 마지막 색은 {}이다.'.format(last_color))

list1 = [1, 2, 3]
# list1.append(4)

print(list1)

list2 = [4, 5, 6]
list1.extend(list2)
list3 = list1
list3 = list1 + list2
print(list3)

numbers = [1, 2, 3, 4, 5]
if 5 in numbers:
    print("5가 있다.")

list1 = [1,2,3]
list1.remove(2)
print(list1)

l = ['가위', '바위', '보']
for i in l:
    print(i, end=' ')

for i in range(4):
    print(i)

# p153 - step2
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
for i in range(len(rainbow)):
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i + 1, color))

# p154 - step3
for i, color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i + 1, color))

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i, day in enumerate(days):
    print('{}월의 날짜 수는 {}일 입니다.'.format( i+1, day))


days_in_month = {
    '1월':31,
    '2월':28,
    '3월':31,
    '-1월':989389829
}

print(days_in_month['1월'])

scores = {
    "김국어":[[100, 100], [100, 50], [10, 100]],
    "박수학":[90, 40, 10]
}

for key, value in scores.items():
    print("{} 학생은 {} {} {} 입니다.".format(key, value[0], value[1], value[2]))

# days_in_month.pop("-1월")
days_in_month.popitem()
# l = [1,2,3]
# del l[2]
# print(l)
# del days_in_month["-1월"]
print(days_in_month)
days_in_month["4월"] = 30
print(days_in_month)


[0,1,2,3,4,100000000]












