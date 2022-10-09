def read_from_file(filename):
    a = []
    with open(filename,'r') as k:
        a = ''.join(x for x in k)
        b = [int(x) for x in a.split(' ')]

    return b

def _max(a):
    k = a[0]
    for x in a:
        if x > k:
            k = x
    return k

def _min(a):
    k = a[0]
    for x in a:
        if x < k:
            k = x
    return k

def _sum(a):
    res = 0
    for x in a:
        res += x
    return res

def _mult(a):
    res = 1
    for x in a:
        res *= x
    return res


