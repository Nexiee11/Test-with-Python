#Note: we do no test empty list(look at the description of an input file. GitHub:demist

def read_from_file(filename):
    a = []
    with open(filename,'r') as k:
        a = ''.join(x for x in k).strip()
        b = [int(x) for x in a.split(' ')]

    return b

def _max(a):
    if len(a) == 0: return 0
    else:
        k = a[0]
        for x in a:
            if x > k:
                k = x
        return k

def _min(a):
    if len(a) == 0: return 0
    else:
        k = a[0]
        for x in a:
            if x < k:
                k = x
        return k

def _sum(a):
    if len(a) == 0: return 0 
    else:
        res = 0
        for x in a:
            res += x
        return res

def _mult(a):
    if len(a) == 0: return 1
    else:
        res = 1
        for x in a:
            res *= x
        return round(res,1)
