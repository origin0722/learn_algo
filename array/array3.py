def remove(nums: list[int], index: int):
    """删除索引 index 处的元素"""
    # 把索引 index 之后的所有元素向前移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i = 1]

"""Drive Code"""
if __name__ == "__main__":
    #初始化数组
    nums = [1, 3, 2, 5, 4]
    print("数组 nums =",nums)

    #删除元素
    remove(nums, 2)
    print("删除索引 2 处的元素，得到 nums =", nums)