#def quadratic(n: int):
#    """平方阶"""
#    # 二维列表占用 O(n^2) 空间
#    num_matrix = [[0] * n for _ in range(n)]

def quadratic_recur(n: int) -> int:
    """平方阶（递归实现）"""
    if n <= 0:
        return 0
    # 数组 nums  长度为 n，n-1，……2，1
    nums = [0] * n
    return quadratic_recur(n - 1)

"""Driver Cdode"""
if __name__ == "__main__":
    n = 5
    print("输入数据大小 n =", n)

    #平方阶
    quadratic_recur(n)

    ###平方阶常见于矩阵和图