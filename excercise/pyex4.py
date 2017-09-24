# 문4. 원의 반지름이 주어져 있을때 원의 면적과 원둘레(원주)의 길이를 구하는 프로그램을 작성하라.
# (단, pi는 아래와 같이 math.pi 값을 사용)
# 원의 면적 = pi * (반지름)의 제곱
# 원둘레(원주)의 길이 = 2 * pi * 반지름
# 실행 예
# 원의 반지름 값(cm)을 입력하세요 : 50
# 원의 면적은 78.54입니다.
# 원둘레의 길이는 31.42입니다.

# 반지름 r값을 받아서, 원의 둘레와 원의 면적을 tuple 형태로 리턴
def circle(r):
    import math
    pi = math.pi

    # r = float(input('원의 반지름 값(cm)을 입력하세요 : '))

    return (pi * r * r, 2 * pi * r)

# print("원의 면적은 {0:5.2f}입니다.".format(pi * r * r))
# print("원둘레의 길이는 {0:5.2f}입니다.".format(2 * pi * r))

# in = float(input('반지름'))
a = circle(10)
print(a[0], a[1])