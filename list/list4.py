# 拼接列表
# 列表拼接操作符 + 将两个列表拼接成一个列表
# 列表乘法操作符 * 将列表重复拼接若干次
# 给定一个新列表 nums1 ，我们可以将其拼接到原列表的尾部
"""Driver Code"""
if __name__ == "__main__":
    nums1 = [1, 3, 2, 5, 4]
    nums2 = [6, 8, 7, 9, 10]
    # 拼接列表
    nums = nums1 + nums2
    print(f"列表 nums1 和 nums2 拼接后的列表为 {nums}")

    # 重复列表
    nums = nums1 * 3
    print(f"列表 nums1 重复拼接 3 次后的列表为 {nums}")
