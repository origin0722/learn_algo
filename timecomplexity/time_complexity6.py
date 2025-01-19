#线性对数阶常出现于嵌套循环中
def linear_log_recur(n:int) -> int:
    """线性对数阶"""
    if n <= 1:
        return 1
    #一分为二，子问题的规模减小一半
    count = linear_log_recur(n//2) + linear_log_recur(n//2)
    # 当前子问题包含n个操作
    for _ in range(n):
        count += 1
        return count

#主流排序算法的时间复杂度通常为线性对数阶
#eg： 排序、归并排序、堆排序等。