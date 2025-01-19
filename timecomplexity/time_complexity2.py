def quadratic(n: int) -> int:
    """平方阶"""
    count = 0
    #循环次数与数据大小n成平方关系
    for i in range(n):
        for j in range(n):
            count +=1
    return count