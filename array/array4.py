def traverse(nums: list[int]):
    """遍历数组"""
    count = 0
    #通过索引遍历数组
    for i in range(len(nums)):
        count += nums
        #同时遍历数据索引和元素
        for i, num in  enumerate(nums):
            count += nums[i]
            count += num

"""Drive Code"""
if __name__ == "__main__":
    #初始化数组
    nums =[1, 3, 2, 5, 4]
    print("数组 num =", nums)

    #遍历数组
    traverse(nums)