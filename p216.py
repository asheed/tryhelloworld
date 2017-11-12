tuple1 = (1,2,3)
tuple2 = 1,2,3
list3 = [1,2,3]
tuple3 = tuple(list3)
tuple4 = tuple([1,2,3])

if tuple1 == tuple2 == tuple3 == tuple4:
    print("tuple1과 tuple2와 tuple3와 tuple4는 모두 같습니다.")

tuple1 = (11, 22, 33)
for i in range( len(tuple1) ):
    print(tuple1[i])