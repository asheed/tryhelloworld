number = 48
print("숫자 맞추기 게임에 오신 것을 환영합니다.")
guess = int(input("1부터 100 사이의 숫자를 추측해보세요: "))

if number == guess:
    print("맞았습니다.")
else:
    print("틀렸습니다.")

print("정답은 {}입니다.".format(number))
print("게임이 종료되었습니다.")
