class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val  #节点值
        self.next: ListNode | None = None # 后继节点引用

def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 p"""
    n1 = n0.next
    P.next = n1
    n0.next = P

"""Drive Code"""
if __name__ == "__main__":
    #初始化链表
    #初始化各个节点
    n0 =ListNode(1)
    n1 =ListNode(3)
    n2 =ListNode(2)
    n3 =ListNode(5)
    n4 =ListNode(4)
    #构建节点之间的引用
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    #插入节点
    p = ListNode(0)
    insert(n0, p)