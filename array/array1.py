import random

def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    #在区间 【0， len（nums） - 1】 中随机抽取一个数字
    random_index = random.randint(0, len(nums) - 1)
    #获取并返回随机元素
    random_num = nums[random_index]
    return random_num

"""Driver Code"""
if __name__ =="__main__":
    #初始化数组
    nums = [1, 3, 2, 5, 4]
