
user_list = ['kimjs', 'tamper', 'lala']
user_password = ['101010', 'pass1234', 'abcd']

name = input('아이디를 입력하세요: ')
if name in user_list:
    i = user_list.index(name)
    password = input('패스워드를 입력하세요: ')
    if password == user_password[i]:
        print('환영합니다. 로그인 되었습니다.')
    else:
        print('잘못된 패스워드 입니다.')
else:
    print('알 수 없는 사용자 입니다.')