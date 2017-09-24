import math

user_input = input("문자열을 입력하세요: ")
length = len(user_input)

if length % 2 == 1: # 홀수
    ch1 = user_input[math.floor(length/2)]
    print("가운데 문자는 {} 입니다".format(ch1))
else:               # 짝수
    ch1 = user_input[math.floor(length/2) - 1]
    ch2 = user_input[math.floor(length/2)]
    print("가운데 문자는 {}, {} 입니다.".format(ch1, ch2))
