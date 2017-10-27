# 문제 132 : 파일쓰기
# 다음 코드로 출력될 내용을 파일 number.txt에 출력하시오(write 혹은 writelines 이용).
# for k in range(10):
# print (k)

with open('number.txt', 'w') as wf:
    for k in range(10):
        wf.write("첫번째 파일 출력 "+ str(k) + "\n")
