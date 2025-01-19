class ListNode:
    """ 链表节点类"""
    def _init_(self, val: int):
        self.val: int = val                #节点值
        self.next: ListNode | None = None  #后继节点引用

def function() -> int:
    """函数"""
    #执行某些操作
    return 0

def constant(n: int):
    """常数阶"""
    #常熟，变量，对象占用O（1）的空间
    a = 0
    nums = [0] * 10
    node = ListNode(0)
    #循环中的变量占用O（1）空间
    for  _ in range(n):
        c = 0
        #循环中的函数占用O（1）空间
        for _ in range(n):
            function()

"""Driver Code"""
if __name__ == "__main__":
    n = 5
    print("输入数据大小 n =", n)

    #常数阶
    constant(n)

    