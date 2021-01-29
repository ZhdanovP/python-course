def exchange(a, b):
    return b, a

def sorter(l, p):
    is_not_sorted = True
    while is_not_sorted:
        is_not_sorted = False
        for i in range(len(l) - 1):
            if not p(l[i], l[i+1]):
                l[i], l[i+1] = exchange(l[i], l[i+1])
                is_not_sorted = True
    return l

x = [2,3,4,1,5,6,7]
print(sorter(x,lambda i,j: i > j))