# 030 문자열 분리
#
# 다음 문자열에 대해 문자열 길이를 기준으로 두 부분으로 분리하여 출력하라.
#
# letters = "introducing python"
# 실행 예:
# 'introduci'
# 'ng python'

letters = "introducing python"
length = int(len(letters)/2)

print(letters[:length])
print(letters[length:])