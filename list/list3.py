#遍历列表
"""Driver Code"""
if __name__ == "__main__":
    nums = [1, 3, 2, 5, 4]

    # 通过索引遍历列表
    count = 0 
    for i in range(len(nums)):
        count += 1
        print(f"元素 {nums[i]} 的索引为 {i}")
    print(f"列表长度为 {count}")

    # 直接遍历列表
    count = 0 
    for num in nums:
        count += 1
        print(f"元素 {num} 的索引为 {count}")
    print(f"列表长度为 {count}")
