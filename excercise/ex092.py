#!/usr/bin/env python
# -*- coding: utf8 -*

# 092 in 연산자
#
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면
# '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
#
# >>> warn_investment_list = ["Nicrosoft", "Doogle", "Never", "KiKio", "SEMSUNG", "HELG"]
# 실행 예:
# 종목 입력: Naver
# 투자 경고 종목이 아닙니다.

warn_investment_list = ["Nicrosoft", "Doogle", "Never", "KiKio", "SEMSUNG", "HELG"]

user_input = input('종목 입력 : ')

if user_input in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')

