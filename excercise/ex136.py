def swap_values(x, y):
    return (y, x)

if __name__ == "__main__":
    a = 3
    b = 4
    #(b, a) = (a, b)
    a, b = swap_values(a, b)

    print("a = {}".format(a))
    print("b = {}".format(b))
