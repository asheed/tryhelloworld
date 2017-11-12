import math

str_number = int(input("절대값을 구할 수를 입력하세요: "))

try:
    number = int(str_number)
except ValueError as ve:
    number = float(str_number)

def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n

print("{}의 절대값은 {}입니다.".format(number, my_abs(number)))

def my_abs2(n):
    return math.sqrt(n*n)

print("{}의 절대값은 {}입니다.".format(number, my_abs2(number)))