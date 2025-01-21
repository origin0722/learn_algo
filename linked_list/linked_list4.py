# 在链表中访问节点的效率较低
# 链表则不然，程序需要从头节点出发，逐个向后遍历，直至找到目标节点
# 因此，链表的访问操作时间复杂度为O(n)
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val  #节点值
        self.next: ListNode | None = None # 后继节点引用

def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

"""Drive Code"""
if __name__ == "__main__":
    #初始化链表
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    #访问节点
    node = access(n0, 3)
    print("链表中索引 3 的节点的值 =", node.val)

