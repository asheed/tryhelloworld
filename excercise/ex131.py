# 문제 131 : 텍스트 파일 읽기 프로그램
# 텍스트 파일을 읽어서 각 라인에 있는 공백으로 분리된 단어의 수를 세는 프로그램을 작성하라. 단, 라인의 첫 문자가 #으로 시작하면 주석문으로 처리하지 않고 넘어간다.
# test.txt
# Its power: python developers typically report
# they are able to develop applications in a half
# #to a tenth the amount of time it takes them to do
# the same work in such languages as C.

s = ''
with open('test.txt', 'r') as f:
# f = open('test.txt', 'r')
    for line in f:
        if line[0] != '#':
            s += line


print(len(s.split()))
