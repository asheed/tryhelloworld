# 문제 135 : 음수, 0, 양수 구별하기
# 사용자로부터 정수를 받아서 음수, 0, 양수 중의 하나로 분류하여 보자.
# 실행 예)
# 정수를 입력하시오: -10
# 입력된 정수는 음수입니다.
# 정수를 입력하시오: 0
# 입력된 정수는 0입니다.

import sys

try:
    num = int(input("정수를 입력하시오: "))
except ValueError as ve:
    print("잘못된 입력입니다!!! 정수를 입력하여야 합니다.")
    print(ve)
    sys.exit(0)

if num > 0:
    print("입력된 정수는 양수입니다.")
elif num < 0:
    print("입력된 정수는 음수입니다.")
else:
    print("입력된 정수는 0입니다.")