def all_func(a):
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
    return _min(a),_sum(a),_mult(a),_max(a)

