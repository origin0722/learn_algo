# 在复杂的系统环境中，程序难以保证数组之后的内存空间是可用的，从而无法安全地扩展数组容量。
# 因此在大多数编程语言中，数组的长度是不可变的
# 请注意，Python 的 list 是动态数组，可以直接扩展
# 为了方便学习，本函数将 list 看作长度不可变的数组
def extend(nums: list[int], enlarge: int) -> list[int]:
    """扩展数组长度"""
    #初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    #将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    # 返回扩展后的数组
    return res

"""Driver Code"""
if __name__ == "__main__":
    #初始化数组
    nums = [1, 3, 2, 5, 4]
    print("数组 nums = ", nums)

    # 长度扩展
    nums = extend(nums, 3)
    print("将数组扩展到 8,得到 nums =", nums)



    