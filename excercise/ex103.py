
password = '3415' # 내가 지정한 비밀번호
count = 0

while True:
    user_password = input('비밀번호 입력 : ') # 사용자로부터 비밀번호를 입력받는다.
    if user_password == password: # 비밀번호가 맞았을 때
        print('맞았습니다. 현관문이 열렸습니다.')
        break
    else: # 비밀번호가 맞지 않았을 때
        print('틀렸습니다. 다시 입력하세요.')
        count += 1
        if count == 5:
            print('비밀번호를 5회 이상 입력하여, 프로그램이 종료됩니다.')
            exit(-1)