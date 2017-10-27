def binary_search(list, item):
    # item : 찾고자 하는 값
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2  # 중간을 구한다.
        guess = list[mid] # 페이지를 펼쳐본다.

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

# print (binary_search(my_list, 3))
# print (binary_search(my_list, -1))
print (binary_search(list(range(10000000)), 4300))