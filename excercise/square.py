from collections import Counter

def solution(v):
    answer = []
    # x = dict(Counter(point[0] for point in v))
    # y = dict(Counter(point[1] for point in v))
    x = Counter(point[0] for point in v)
    y = Counter(point[1] for point in v)
    for key,value in x.items():
        if value == 1:
            answer.append(key)

    for key, value in y.items():
        if value == 1:
            answer.append(key)

    return answer

v1 = [[1,4],[3,4],[3,10]]
v2 = [[1,1],[2,2],[1,2]]

print(solution(v1))
print(solution(v2))