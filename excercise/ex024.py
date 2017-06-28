# 024 문자열의 마지막 패턴 매칭
#
# 파일 이름이 다음과 같을 때 확장자가 .py 이면 'python file'를 출력하고
# 아니면 'unknown extension'을 출력하는 프로그램을 작성하라.
#
# filename = "run.py"
# 출력 예:
# python file

filename = "run.py"

if filename.split('.')[1] == 'py':
    # 위 예에서 filename.split('.')의 결과는 아래와 같다.
    # ['run', 'py']
    print('python file')
else:
    print('unknown extension')