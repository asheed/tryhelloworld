
# def ready(at):
#     n = int(at)
#     n_chicken = n
#     n_coke = n * 2
#     n_cake = n * 4
#     n_cookie = n * 2
#     (n_table, other) = divmod(n, 4)
#     if other != 0:
#         n_table += 1
#
#     return [n_chicken, n_coke, n_cake, n_cookie, n_table]

ready_item = {"치킨":0, "콜라":0, "케이크":0, "과자":0, "탁자":0}

def ready(at, dic):
    n = int(at)
    dic["치킨"] = n
    dic["콜라"] = n * 2
    dic["케이크"] = n * 4
    dic["과자"] = n * 2
    (dic["탁자"], other) = divmod(n, 4)
    if other != 0:
        dic["탁자"] += 1


attendant = input("참석자의 수를 입력하세요 : ")

ready(attendant, ready_item)

print("치킨의 수 : {}".format(ready_item["치킨"]))
print("콜라의 수 : {}".format(ready_item["콜라"]))
print("케이크의 수 {}".format(ready_item["케이크"]))
print("과자의 수 {}".format(ready_item["과자"]))
print("탁자의 수 {}".format(ready_item["탁자"]))
