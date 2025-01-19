#对数阶反映了“每轮缩减到一半”的情况。
def logarithmic(n:int) -> int:
    """对数阶（循环实现）"""
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

def log_recur(n: int) -> int:
    """对数阶（递归实现）"""
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1

#对数阶常出现于基于分治策略的算法中，体现了“一分为多”和“化繁为简”的算法思想。
#它增长缓慢，是仅次于常数阶的理想的时间复杂度。


#while循环只会执行logn次，复杂度是logn