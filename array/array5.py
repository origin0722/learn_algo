# 查找元素
# 在数组中查找指定元素需要遍历数组
# 每轮判断元素值是否匹配，若匹配则输出对应索引
# 因为数组是线性数据结构，所以上述查找操作被称为“线性查找”

def find(nums: list[int], target: int) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        return -1
    
"""Drive COde"""
if __name__ == "__main__":
    #初始化数组
    nums = [1, 3, 2, 5, 4]
    print("数组 nums =", nums)

    #查找元素
    index: int = find(nums, 3)
    print("在 nums  中查收元素 3 , 得到索引 =", index)
    
