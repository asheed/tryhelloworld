# 사용자 입력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값을 출력하는 프로그램을 작성하라.
# 실행 예:
# first: 3
# second: 4
# 합:  7

# http://hashcode.co.kr/questions/2325/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EC%9E%85%EB%A0%A5%EA%B0%92%EC%9D%84-%EC%A0%95%EC%88%98%EB%A1%9C-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95
# https://stackoverflow.com/questions/21122540/input-error-nameerror-name-is-not-defined/21122817#21122817
first = input("first: ")
second = input("second: ")
try:
    print("합:", int(first) + int(second))
    print("합:", first + second)
except ValueError as ve:
    print("입력되는 데이터는 숫자만 허용됩니다.")
