# 021 문자열 합치기
#
# 리스트에 회사 이름이 저장되어 있다. 각 회사 이름이 구분자 ";"로 연결된 문자열을 생성하라.
#
# >>> companies = ['NAVER', 'KAKAO', 'SK', 'SAMSUNG']
# 실행 예:
# >>> nstring
# 'NAVER;KAKAO;SK;SAMSUNG'

companies = ['NAVER', 'KAKAO', 'SK', 'SAMSUNG']

nstring = ';'.join(companies)
print(nstring)
