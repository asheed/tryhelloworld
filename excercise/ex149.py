# 문제 149 : 자리수의 합 구하기
# 정수 안의 각 자리수의 합을 계산하는 프로그램을 작성해보자. 예를 들어서 1234이면 (1 + 2 + 3 + 4)를 계산한다.
# 실행결과)
# 정수를 입력하세요 : 4040
# 자리수의 합은 8 입니다.
# 정수를 입력하세요 : 12345
# 자리수의 합은 15 입니다.
number = int(input("정수를 입력하세요 : "))
result = 0
while number > 0:
    digit = number % 10
    result = result + digit
    number = number // 10
print("자리수의 합은 {}입니다.".format(result))
