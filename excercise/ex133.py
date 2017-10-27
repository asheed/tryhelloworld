# 문제 133 : 임금 계산
# 사용자에게 근무 시간과 시간당 임금을 물어본다.
# 주당 근무 시간이 40시간을 넘으면 1.5배의 임금을 지급해야한다고 하자.
# 이번 주에 받는 총 임금을 계산하는 프로그램을 작성해보자.
# 실행 예)
# 근무시간을 입력하세요: 45
# 시간당 임금을 입력하세요: 5000
# 총 임금은  237500.0 원입니다.

work_hour = int(input("근무시간을 입력하세요: "))
pay_per_hour = int(input("시간당 임금을 입력하세요: "))

if work_hour > 40:
    total_pay = 40 * pay_per_hour + (work_hour - 40) * pay_per_hour * 1.5
else:
    total_pay = work_hour * pay_per_hour

print("총 임금은 {} 원입니다.".format(total_pay))
