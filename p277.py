def safe_index(a_list, value):
    # 함수를 완성하세요
    try:
        return a_list.index(value)
    except ValueError as e:
        return None

def safe_index2(a_list, value):
    if value in a_list:
        return a_list.index(value)
    else:
        return None


list1 = [1, 2, 3, 4]
print(safe_index(list1, 1))     # 0
print(safe_index(list1, 100))   # None

