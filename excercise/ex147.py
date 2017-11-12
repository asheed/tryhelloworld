# 문제 147 :  정수의 합 계산하기(반복)
# For 문을 이용하여 정수의 합을 계산해보자.
# 1부터 사용자가 입력한 수 n까지 더해서 (1+2+3+…+n)을 계산하는 프로그램을 작성해 보자.
# for문과 range함수를 사용하면 간단하게 합계를 구할 수 있다.
# 실행결과)
# 몇까지의 합을 계산할까요? 10
# 1부터 10까지의 정수의 합 = 55

def my_sum(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

if __name__ == '__main__':
    num = int(input("몇까지의 합을 계산할까요? "))
    print("1부터 {}까지의 정수의 합 = {}".format(num, my_sum(num)))