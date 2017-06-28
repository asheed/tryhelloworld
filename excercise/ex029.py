# 029 도메인 추출
#
# 사용자로부터 웹 페이지 주소를 입력 받은 후 도메인을 출력하라.
# 도메인은 .com, .net, .org 만 지원한다. www는 반드시 입력된다.
#
# 실행 예:
# address: http://www.wikidocs.net/edit/page/7022
# domain: net

domain_list = ['.com', '.net', '.org']
address = input('address: ')
# 방법1
# found_domain = [domain for domain in domain_list if domain in address]
# print('domain:', found_domain[0][1:])

# 방법2
# found_domain = []
# for domain in domain_list:
#     if domain in address:
#         found_domain.append(domain)
#
# if not found_domain:    # domain 정보를 찾지못했다..가 참이면
#     print('입력한 주소에서 도메인 정보를 찾을 수 없습니다!!!')
# else:
#     print('domain:', found_domain[0][1:])

## 방법3 : http://www. 가 반드시 입력된다고 가정했을때
domain_list2 = ['com', 'net', 'org']
domain = address.split('/')[2].split('.')[2]
if domain in domain_list2:
    print('domain:', domain)


