
# 재귀를 이용한 팩토리얼 구하기

num = int(input('정수를 입력하세요: '))

def my_factorial(n):
    if n == 1:
        return 1
    return n * my_factorial(n-1)

print('{}!은 {}이다.'.format(num, my_factorial(num)))
