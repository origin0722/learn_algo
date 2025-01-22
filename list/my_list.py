# 列表的实现
# 初始容量：选取一个合理的数组初始容量。在本示例中，我们选择 10 作为初始容量
# 数量记录：声明一个变量 size ，用于记录列表当前元素数量，并随着元素插入和删除实时更新。根据此变量，我们可以定位列表尾部，以及判断是否需要扩容
# 扩容机制：当 size 达到容量上限时，我们进行扩容，即申请一个更大的数组，并将原数组中的所有元素搬移至新数组。在本示例中，我们选择扩容至 2 倍
# 缩容机制：当 size 小于容量的一半时，我们进行缩容，即申请一个更小的数组，并将原数组中的所有元素搬移至新数组。在本示例中，我们选择缩容至 1/2
# 插入元素：当插入元素时，我们首先检查是否需要扩容。如果需要，则进行扩容；随后将新元素添加到数组尾部，并更新 size 。
# 删除元素：当删除元素时，我们首先检查是否需要缩容。如果需要，则进行缩容；随后将尾部元素删除，并更新 size 。
# 访问元素：当访问元素时，我们只需返回数组指定下标处的元素，并更新 size 。
# 遍历列表：当遍历列表时，我们只需使用一个 for 循环，从 0 遍历至 size - 1 ，依次访问每个元素。    
class MyList:
    """MyList 的实现 列表类"""
    def  __init__(self):
        self._capacity = 10  # 列表容量
        self._arr: list[int] = [0] * self._capacity # 数组（存储列表元素）
        self._size: int = 0  # 列表元素数量(列表长度)
        self._extens_ratid: int = 2 # 每次列表扩容的的倍数

    def size(self) -> int:
        """获取列表当前长度（即元素数量）"""
        return self._size
    
    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity
    
    def get(self, index: int) -> int:
        """访问元素"""
        # 若索引越界，则抛出异常
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    
    def set(self, num: int, index: int) -> None:
        """更新元素"""
        # 若索引越界，则抛出异常
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num: int) -> None:
        """向列表尾部添加元素"""
        # 若列表已满，则进行扩容
        if self._size == self._capacity:
            self._extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int) -> None:
        """在列表指定位置插入元素"""
        if index < 0 or index > self._size:
            raise IndexError("索引越界")
        # 元素数量超出容量，触发扩容机制
        if self._size == self._capacity:
            self._extend_capacity()
        # 将索引 index 以及之后的元素向后移动一位
        for i in range(self._size - 1, index - 1, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[index] = num
        self._size += 1

    def remove(self, index: int) -> int:
        """删除列表指定位置的元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        # 将索引 index 之后的元素向前移动一位
        for i in range(index, self._size - 1):
            self._arr[i] = self._arr[i + 1]
        self._size -= 1
        return num
    
    def _extend_capacity(self) -> None:
        """扩容列表"""
        #新建一个长度为原数组 ——extend_ratio倍 的数组，并将原数组中的所有元素搬移至新数组
        self._arr = self._arr + [0] * self._capacity * (self._extens_ratio - 1)
        #更新列表容量
        self._capacity = len(self._arr)
    
    def to_array(self) -> list[int]:
        """返回列表的数组形式"""
        return self._arr[:self._size]
    

"""Driver Code"""
if __name__ == "__main__":
    # 初始化列表
    nums = MyList()
    # 尾部添加元素
    nums.add(1)
    nums.add(3)
    nums.add(2)
    nums.add(5)
    nums.add(4)
    print("列表 nums = {}".format(nums.to_array()))

    # 在中间插入元素
    nums.insert(6, index = 3)

    #删除元素
    nums.remove(3)

    #访问元素
    print("访问元素 nums[1] = {}".format(nums.get(1)))

    #更新元素
    nums.set(0, 1)
    print("更新后的列表 nums = {}".format(nums.to_array()))

    #遍历列表
    for i in range(nums.size()):
        print("列表的第 {} 个元素 = {}".format(i, nums.get(i)))

    #测试扩容机制
    for i in range(10):
        nums.add(i)


