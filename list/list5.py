#  排序列表
# 给定一个列表 nums ，我们可以对其进行排序，使其元素按升序或降序排列
# 列表的 sort() 方法可以对列表进行原地排序，即直接在原列表上进行操作，不返回新列表
# 列表的 sorted() 函数可以对列表进行排序，并返回新列表，不改变原列表
# 列表的 reverse() 方法可以反转列表，即列表元素从后向前排列
# 列表的 reversed() 函数可以反转列表，并返回新列表，不改变原列表
# 完成列表排序后，我们便可以使用在数组类算法题中经常考查的“二分查找”和“双指针”算法
"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 2, 5]
    # 排序列表
    nums.sort()
    print(f"列表 nums 排序后为 {nums}")

    # 排序列表
    nums = sorted(nums)
    print(f"列表 nums 排序后为 {nums}")

    # 反转列表
    nums.reverse()
    print(f"列表 nums 反转后为 {nums}")

    # 反转列表
    nums = reversed(nums)
    print(f"列表 nums 反转后为 {nums}")
