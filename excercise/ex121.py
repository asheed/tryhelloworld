my_dict = {
    'a':'w', 'b':'x', 'c':'y', 'd':'z',
    'w':'a', 'x':'b', 'y':'c', 'z':'d'
}

s = input("문자열을 입력하세요 : ")

result = ''
for c in s: # s = 'cabsz'
    if c in my_dict.keys():
        result += my_dict[c]
    else:
        result += c

print("변환 문자열 : {}".format(result))
