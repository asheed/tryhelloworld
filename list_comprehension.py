areas = []
for i in range(1,11):
    if i % 2 == 0:
        areas.append(i*i)

areas2 = [i*i for i in range(1, 11) if i % 2 == 0]

print("areas:", areas)
print("areas2:", areas2)

list1 = [i for i in range(1,101) if i % 8 == 0]
print(list1)
print(len(list1))
