# 문제 10-3. 함수 sum을 정의하라. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산한다.
# 예를 들면 sum()은 0을 sum(1,2)는 3을 sum(1,5,7,2,3)은 18을 리턴한다.
# 힌트 : 가변 인수

def sum(*kw):
    res = 0
    if not kw:
        return 0
    else:
        for n in kw:
            res += n
        return res

if __name__ == "__main__":
    print(sum())
    print(sum(1,2))
    print(sum(1,5,7,2,3))