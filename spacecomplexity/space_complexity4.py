class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int = 0):
        self.val: int = val  #节点值
        self.left: TreeNode | None = None #左子节点引用
        self.right:TreeNode | None = None #右子节点引用

def build_tree(n: int) -> TreeNode | None:
    """指数阶（建立满二叉树）"""
    if n == 0:
        return None
    root = TreeNode(0)
    root.left = build_tree(n - 1)
    root.right = build_tree(n - 1)
    return root

"""Driver Code"""
if __name__ == "__main__":
    n = 5
    print("输入数据大小n =", n)

    # 指数阶
    root = build_tree(n)

    