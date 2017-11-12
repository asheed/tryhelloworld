import time
# 반복을 이용한 팩토리얼 구하기
result = 1
n = int(input('정수를 입력하세요: '))

def fact(n):
    for i in range(1, n+1):
        result = result * i
    return result

print('{}!은 {}이다.'.format(n, fact(n)))


