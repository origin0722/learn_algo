def linear(n: int):
    """线性阶"""
    # 长度为 n 的列表占用 O（n） 空间
    nums =[0] * n
    # 长度为n 的哈希表占用O（n） 空间
    hump = dict[int,str]()
    for i in range(n):
        hump[i] = str(i)

"""Drive Code"""
if __name__ =="__ mian__":
    n = 5
    print("输入数据大小 n =", n)

    #线性阶
    linear(n)

    ###常数阶常见于数量与输入数据大小 n
    ###无关的常量、变量、对象。
