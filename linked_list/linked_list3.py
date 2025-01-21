class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val  #节点值
        self.next: ListNode | None = None # 后继节点引用

def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    p = n0.next
    n1 = p.next
    n0.next = n1

"""Drive Code"""
if __name__ == "__main__":
    #初始化链表
    #初始化各个节点
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)
    #构建节点之间的引用
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    #删除节点
    remove(n0)
    print(n0.next.val)

    ##在链表中删除节点也非常方便，只需改变一个节点的引用（指针）即可