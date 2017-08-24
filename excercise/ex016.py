# 016 문자열 거꾸로 뒤집기
#
# 문자열을 거꾸로 뒤집어 출력하라.
#
# >>> input = "PYTHON"
# 실행 예:
# >>> output
# 'NOHTYP'

input = "PYTHON"
output = input[-1::-1]
# print(input[0:6:2])
# print(output)

i = len(input)
while i>=1:
    print(input[i-1],end='')
    i -= 1