def sum(*args):
    res = 0
    for n in args:
        res += n
    return res

def sum2(*kw):
    res = 0
    if not kw:
        return 0
    else:
        for n in kw:
            res += n
        return res


if __name__ == "__main__":
    print(sum())
    print(sum(1,2))
    print(sum(1,5,7,2,3))