steps = 0


def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print(startPeg, "번 기둥의", ndisks, "번 원반을", endPeg, "번 기둥으로 옮깁니다.")
        hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)


hanoi(ndisks=10)
