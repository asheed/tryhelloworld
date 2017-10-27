# 문제 138 : 계산 로봇 알고리즘 구현하기
# 칠성이는 마트에서 계산을 하는 로봇의 알고리즘을 구현하려고 한다.
# 구매금액을 확인하였을 때, 계산대에 내야 하는 최소한의 지폐와 동전의 수를 출력하세요.
# (거스름돈을 받지 않는다고 가정)
# 실행 예)
# 구매 금액을 입력하세요: 45430
# 내야할 지폐와 동전
# 오만원 : 0 매
# 만원 : 4 매
# 오천원 : 1 매
# 천원 : 0 매
# 오백원 : 0 개
# 백원 : 4 개
# 오십원 : 0 개
# 십원 : 3 개

amount = int(input("구매 금액을 입력하세요(10원 단위까지 입력) : "))
bill_list = [0, 0, 0, 0, 0, 0, 0, 0]
bill_unit_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i, v in enumerate(bill_unit_list):
    bill_list[i] = amount // v  # 50000원권 갯수
    amount -= bill_list[i] * v

print("내야할 지폐와 동전")

for i, v in enumerate(bill_unit_list):
    print("{} : {}".format(v, bill_list[i]))
