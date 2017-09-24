import random
number = random.randint(1,100)
print("숫자 맞추기 게임에 오신 것을 환영합니다.")
guess = -1

while number != guess: # 틀렸을 때
    user_input = input("1부터 100 사이의 숫자를 추측해보세요 (종료하려면 q를 입력하세요): ")
    if user_input[0].lower() == 'q':
        break

    guess = int(user_input)
    if number == guess:
        print("맞았습니다.")
        break
    else:
        if guess > number:
            print("틀렸습니다. 정답은 입력하신 {}보다 작습니다. 잘 생각해 보세요".format(guess))
        else:
            print("틀렸습니다. 정답은 입력하신 {}보다 큽니다. 잘 생각해 보세요".format(guess))

print("정답은 {}입니다.".format(number))
print("게임이 종료되었습니다.")
