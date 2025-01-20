def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素 num"""
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将 num 赋给 index 处的元素
    nums[index] = num

    """Drive Code"""
    if __name__ == "__main__":
        #初始化数组
        nums = [1, 3, 2 ,5 ,4]
        print("数组 nums =",nums)

        #插入元素
        insert(nums, 6, 3)
        print("在索引 3 处插入数字 6 ，得到 nums =",nums)