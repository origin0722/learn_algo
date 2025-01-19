def linear_recur(n: int):
    """线性阶（递归实现）"""
    print("递归 n =",n)
    if n == 1:
        return
    linear_recur(n - 1)

    """Driver Code"""
    if __name__ == "__main__":
        n = 5
        print("输入数据大小 n =",n)

        #线性阶 
        linear_recur(n)

        ###线性阶常见于元素数量与 n
        ###成正比的数组、链表、栈、队列等：