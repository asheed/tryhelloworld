# 문3. 화씨를 섭씨로 변환하는 프로그램을 작성하라.
# 섭씨 = (화씨 - 32) * 5.0 / 9.0
# 참고 http://www.metric-conversions.org/ko/temperature/fahrenheit-to-celsius.htm
# 실행 예
# 변환할 온도를 화씨 기준으로 입력하세요 : 50
# 화씨 50도는 섭씨 10.0도 입니다.

f = input('변환할 온도를 화씨 기준으로 입력하세요 : ')
print('화씨 {0:s}도는 섭씨 {1:4.2f}도 입니다.'.format(f, (float(f)-32)*5.0/9.0))
