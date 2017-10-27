# 문1002. 터렛

# https://www.acmicpc.net/problem/1002
#
# 조규현과 백승환은 터렛에 근무하는 직원이다.
# 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다.
#
# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
# 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
#
# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
#
# 입력
#
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.
#
# 첫째 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
# x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
#
# 출력
#
# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
#
# 예제 입력
#
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5
#
# 예제 출력
#
# 2
# 1
# 0

# input
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5

import math

def D(P1, P2, r1, r2):
    plus_r = r1 + r2 # 두 원의 반지름의 합
    minus_r = abs(r1 - r2) # 두 원의 반지름의 차
    p2p = math.sqrt(math.pow(P2[0]-P1[0], 2) + math.pow(P2[1]-P1[1], 2)) # 원의 중심 사이의 거리
    if P1 == P2 and r1 == r2: # 무한
        return -1
    elif P1 == P2: # 동심원
        return 0
    elif p2p > plus_r or p2p < minus_r:
        return 0
    elif p2p == plus_r or p2p == minus_r: # 외접 또는 내접
        return 1
    elif p2p < plus_r and p2p > minus_r:
        return 2
    else:
        return 0

T = int(input()) # testcase
l = [input() for _ in range(T)]
for i in l:
    t = i.split()
    P1 = tuple(map(int, t[0:2]))
    r1 = int(t[2])
    P2 = tuple(map(int, t[3:5]))
    r2 = int(t[5])
    print(D(P1, P2, r1, r2))
