# 查找节点 
# 遍历链表，查找其中值为 target 的节点，输出该节点在链表中的索引。此过程也属于线性查找
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val # 节点值
        self.next: ListNode | None = None #后继节点引用

def find(head: ListNode, target: int) -> int:
        """查找链表中值为 target 的首个节点"""
        index = 0
        while head:
            if head.val == target:
                return index
            head = head.next
            index += 1
        return -1
    
"""Driver Code"""
if __name__ == "__main__":
    #初始化链表
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

    #查找节点
    index = find(n0, 2)
    print("目标节点索引为  =",format(index))
