def bubble_sort(nums: list[int]) -> int:
    """平方阶（冒泡排序）"""
    count = 0 #计数器
    #外循环： 未排序区间为[0,1]
    for i in range(len(nums) -1,0,-1):
        #内循环：将未排序区间[0,1]中最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j] > nums[j+1]:
                #交换 nums[j]与nums[j+1]
                tmp:int = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                count += 3 #元素交换包含3个单元操作
    return count