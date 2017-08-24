def print_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))


x = 2
y = -6
z = -8

print_root(x, y, z)

# a = 1
# b = 2
# c = -8

#print_root(1, 2, -8)
# print_root()

# a = 2
# b = -6
# c = -8

#print_root(2, -6, -8)
# print_root()

# a = int(input("a값을 입력하세요: "))
# b = int(input("b값을 입력하세요: "))
# c = int(input("c값을 입력하세요: "))
#
# print_root(a, b, c)

#
# def function(a):
#     print("안녕하세요\n"*a)
#
# function(10)


# def add(a, b):
#     a = a + 1
#     b = b * 2
#     print(a+b)
#
#
# print('3 + 5 = ', add(3, 5))





