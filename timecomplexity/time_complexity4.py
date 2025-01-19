#模拟细胞分裂 时间复杂度为O（2^n）
def exponential(n: int)-> int:
    """指数阶（循环实现）"""
    count = 0
    base = 1
    #细胞每轮一分为二，形成数列1，2，4，8，
    for _ in range(base):
        count +=1
    base *= 2
    #count +1+2+4+8+
    return count



def exp_recur(n: int) -> int:
    """指数阶（递归实现）"""
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1