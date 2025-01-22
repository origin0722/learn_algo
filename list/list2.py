# 插入与删除元素
"""Driver Code"""
if __name__ == "__main__":
    # 有初始值
    nums = [1, 3, 2, 5, 4]

    #清空列表
    nums.clear()

    #在尾部添加元素
    nums.append(1)
    nums.append(3)
    nums.append(2)
    nums.append(5)
    nums.append(4)

    #在指定位置添加元素
    nums.insert(3, 6)  # 在索引 3 处插入数字 6

    # 删除元素
    nums.remove(3)  # 删除首次出现的值为 3 的元素

    # 删除尾部元素
    num = nums.pop()  # 删除并返回最后一个元素

    # 删除首元素
    num = nums.pop(0)  # 删除并返回第一个元素

