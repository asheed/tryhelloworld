# 문제 150 : 최대 공약수 구하기
# 최대 공약수란 정수들의 공통 약수 중에서 가장 큰 수를 의미한다.
# 예를 들어서 8과 12의 최대 공약수는 8의 약수 1, 2, 4, 8과 12의 약수 1, 2, 3, 4, 6, 12 중 공통하는 가장 큰 수인 4가 된다.
# 최대 공약수를 구하려면 정교한 수학적 알고리즘이 필요하다.
# 최대 공약수를 구하는 알고리즘은 기원전 300년 전에 이미 유클리드에 의하여 개발되었다.
# 따라서 여기서는 그 알고리즘을 구현하는 데만 초점을 맞추어보자.
# 유클리드 호제법
# 1.	두 수 가운데 큰 수를 x, 작은 수를 y라고 한다.
# 2.	y가 0이면 최대 공약수는 x와 같고 알고리즘을 종료한다.
# 3.	x를 y로 나눈 나머지를 r이라고 하자.
# 4.	y를 x에 대입한다.
# 5.	r을 y에 대입한다.
# 6.	2번으로 돌아간다.
# 위 알고리즘을 프로그램으로 작성하세요.
# 실행결과)
# 두 수를 입력하세요 : 8 12
# 최대 공약수는 4 입니다.
# 두 수를 입력하세요 : 1071 1029
# 최대 공약수는 21 입니다.
# 두 수를 입력하세요 : 78696 19332
# 최대 공약수는 36 입니다.

num_list = input("두 수를 입력하세요 : ").split()
if int(num_list[0]) > int(num_list[1]):
    x = int(num_list[0])
    y = int(num_list[1])
else:
    x = int(num_list[1])
    y = int(num_list[0])

while (y != 0):
    r = x % y
    x, y = y, r
print("최대 공약수는 {}입니다.".format(x))