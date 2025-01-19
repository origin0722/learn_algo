def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count = 0
    #从一个分裂出n个
    for _ in range(n):
        count += factorial_recur(n - 1)
        return count
    
    #阶乘阶比指数阶增长得更快，在n较大时也是不可接受的。