# 015 문자열 분리
#
# 영상의 크기를 resolution이 바인딩하고 있을 때 영상의 너비와 높이를 출력하라. 예를 들어, "176x144"이면 너비가 176 높이가 144이다.
#
# >>> resolution = '1920x1080'
# width: 1920
# height: 1080

resolution = '1920x1080'
wid_height = resolution.split('x')
print('width:', wid_height[0])
print('height:', wid_height[1])