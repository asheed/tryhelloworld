#!/usr/bin/env python
# -*- coding: utf8 -*

# 094 주민등록번호를 이용한 출생지 알아보기
#
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미합니다. 다음 표를 참조하여 사용자로부터 주민 등록 번호를 입력 받은 후 출생지를 출력하는 프로그램을 작성하라.
#
# 지역 코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# 13 ~ 15	인천
# 16 ~ 25	경기도
# 26 ~ 34	강원도
# 35 ~ 39	충청북도
# 41 ~ 47	충청남도
# 48 ~ 55	전라북도
# 56 ~ 64	전라남도
# 70 ~ 80	경상북도
# 81 ~ 99 (85제외)	경상남도
# 40	대전 광역시
# 65 ~ 66	광주 광역시
# 67 ~ 69	대구 광역시
# 85	울산 광역시
# 실행 예:
# 주민등록번호: 821010-1635210
# 전라남도

jumin_no = input('주민등록번호: ')

area_code = int(jumin_no.split('-')[1][1:3])

if area_code >= 0 and area_code <= 8:
    print('서울 특별시')
elif area_code >= 9 and area_code <= 12:
    print('부산 광역시')
elif area_code >= 13 and area_code <= 15:
    print('인천 광역시')
elif area_code >= 16 and area_code <= 25:
    print('경기도')
elif area_code >= 26 and area_code <= 34:
    print('강원도')
elif area_code >= 35 and area_code <= 39:
    print('충청북도')
elif area_code >= 41 and area_code <= 47:
    print('충청남도')
elif area_code >= 48 and area_code <= 55:
    print('전라북도')
elif area_code >= 56 and area_code <= 64:
    print('전라남도')
elif area_code >= 70 and area_code <= 80:
    print('경상북도')
elif (area_code >= 81 and area_code <= 84) or (area_code >= 86 and area_code <= 99):
    print('경상남도')
elif area_code == 40:
    print('대전 광역시')
elif area_code in (65, 66):
    print('광주 광역시')
elif area_code in (67, 68, 69):
    print('대구 광역시')
elif area_code == 85:
    print('울산 광역시')
else:
    print('유효하지 않습니다.')
