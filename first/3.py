def tail_recur(n,res):
    if n == 0:
        return res
    return tail_recur(n-1,res+n)