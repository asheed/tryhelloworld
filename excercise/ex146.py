import time
import sys
n = int(input("초기숫자를 입력하세요: "))
# while n > 0:
#     print(n, end=' ')
#     time.sleep(1)
#     sys.stdout.flush()
#     n -= 1

for i in range(n, 0, -1):
    print(i, end=' ')
    time.sleep(1)
    sys.stdout.flush()

time.sleep(1)
print("발사")