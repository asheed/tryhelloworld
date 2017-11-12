import getpass
user_list = {
    'kimjs': '101010',
    'tamper': 'pass1234',
    'lala': 'makers'
}

name = input('아이디를 입력하세요: ')
if name in user_list:
    # password = input('패스워드를 입력하세요: ')
    password = getpass.getpass('패스워드를 입력하세요: ')
    if user_list[name] == password:
        print('환영합니다. 로그인 되었습니다.')
    else:
        print('잘못된 패스워드 입니다.')
else:
    print('알 수 없는 사용자 입니다.')