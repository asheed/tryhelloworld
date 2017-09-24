# 문제 10-4. 이미지 파일을 작게 표시하기 위한 썸네일thumb nail)이라는 작은 이미지 파일들이 있다.
# 이 파일들은 원래의 이미지 파일에 _thumb란 이름이 추가로 붙는다.
# 예를 들면 a.jpg의 썸네일 파일은 a_thumb.jpg이다.
# 이미지 파일 이름들이 아래와 같이 리스트에 담겨 있을 때 filter 함수를 이용하여 여기서 썸네일 파일만 골라내어 출력하라.

img_list = ['a.jpg', 'a_thumb.jpg', 'cc.jpg', 'd_thumb.jpg', 'zzzz_thumb.jpg']

print(list(filter(lambda x:'_thumb' in x, img_list)))
