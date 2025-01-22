def function() -> int:
    #执行某些操作
    return 0

def loop(n: int):
    """循环的空间复杂度为O(1)"""
    for _ in range(n):
        function()

def recur(n: int):
    """递归的空间复杂度为O(n)"""
    if n == 1:
        return
    return recur(n - 1)
