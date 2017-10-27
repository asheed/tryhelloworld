# 문제 137 : 양의 값만 출력하는 함수
# 리스트를 입력받아 양의 값만 골라 리스트로 반환하는 함수 positive를 작성하라.
# 함수의 모양은 아래와 같다.

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)

    return result

print(positive([1, -3, 2, 0, -5, 6, 100, -10, 0.1, -0.1]))

# filter 와 lambda 를 사용하면 코드를 더 간결하게 짤 수 있어요!!
