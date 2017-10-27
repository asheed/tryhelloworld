# 문제 141 : 예외처리
# 예외 처리를 이용하여 변수가 정의되지 않은 경우를 처리하라.
# 예를 들면 price = selected라는 문에서 만일 selected가 앞서 정의되지 않았다면 NameError를 일으킨다.
# selected가 정의되지 않은 경우에 price의 값을 0으로 설정하는 코드를 작성하세요.
selected = 1000
try:
    price = selected
except NameError as e:
    print(e.args)
    price = 0
finally:
    print("선택된 제품의 금액은 {}원 입니다.".format(price))

# print(price)
#위 코드를 실행하면 NameError 발생
#try … except 문을 사용해서, 처리하세요.
