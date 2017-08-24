def caesar(s, n):
    l_table = "abcdefghijklmnopqrstuvwxyz"
    u_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i, tmp in enumerate(s):
        if tmp == ' ':
            result += ' '
        else:
            if tmp >= 'a' and tmp <= 'z':
                result += l_table[(l_table.find(tmp) + n) % 26]
            elif tmp >= 'A' and tmp <= 'Z':
                result += u_table[(u_table.find(tmp) + n) % 26]

    return result
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))