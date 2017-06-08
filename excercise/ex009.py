# 사칙 연산
# 사용자로부터 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.
'''
실행 예:
first number: 10
second number: 2
add:  12
sub:  8
mul:  20
div:  5.0
'''
a = input("첫번째 수를 입력하세요: ")
b = input("두번째 수를 입력하세요: ")
print("입력한 두 수의 덧셈 결과는", int(a) + int(b))
print("입력한 두 수의 뺄셈 결과는", int(a) - int(b))
print("입력한 두 수의 곱셈 결과는", int(a) * int(b))
print("입력한 두 수의 나눗셈 결과는", int(a) / int(b))