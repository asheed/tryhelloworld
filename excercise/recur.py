
def my_sum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + my_sum(l[1:])

my_sum([1,2,3])
