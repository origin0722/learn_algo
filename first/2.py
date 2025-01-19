def recur(n:int) -> int:
    if n==1:
        return 1
    res = recur(n-1)
    return n + res
