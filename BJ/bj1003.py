countKey = {'0':0, '1':0}
memo = {1:1, 2:1}
def fib(n):
    global countKey
    if n == 0:
        #print(0)
        countKey['0'] += 1
        return 0
    if n == 1:
        #print(1)
        countKey['1'] += 1
        return 1
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    # else:
    #     return fib(n-1) + fib(n-2)

T = int(input()) # testcase
call_list = [int(input()) for _ in range(T)]

if __name__ == '__main__':
    for i in call_list:
        countKey = {'0':0, '1':0}
        fib(i)
        print(str(countKey['0']) + " " + str(countKey['1']))