"""
Numpy简介
    NumPy（Numerical Python）是Python数据分析必不可少的第三方库
    NumPy的出现一定程度上解决了Python运算性能不佳的问题，同时提供了更加精确的数据类型，使其具备了构造复杂数据类型的能力
    本身是由C语言开发，是个很基础的扩展，NumPy被Python其它科学计算包作为基础包，因此理解np的数据类型对python数据分析十分重要
    NumPy重在数值计算，主要用于多维数组（矩阵）处理的库。用来存储和处理大型矩阵，比Python自身的嵌套列表结构要高效的多
Numpy重要功能
    1. 高性能科学计算和数据分析的基础包
    2. ndarray，多维数组，具有矢量运算能力，快速、节省空间
    3. 矩阵运算，无需循环，可完成类似Matlab中的矢量运算
    4. 用于读写磁盘数据的工具以及用于操作内存映射文件的工具
Numpy的属性
    NumPy的数组类被称作ndarray，通常被称作数组。
    ndarray.ndim
    ndarray.shape
    ndarray.size
    ndarray.dtype
    ndarray.itemsize
    数组的维度
        这是一个指示数组在每个维度上大小的整数元组。例如一个n排 m列的矩阵，它的shape属性将是(2,3),这个元组的长度显然是秩，即维度或者ndim属性。ndarray介绍
ndarray介绍
    NumPy数组是一个多维的数组对象（矩阵），称为]ndarray(N-Dimensional Array)
    具有矢量算术运算能力和复杂的广播能力，并具有执行速度快和节省空间的特点
    注意：ndarray的下标从0开始，且数组里的所有元素必须是相同类型
zeros()/ones()/empty()/arange()/matrix()
    函数zeros创建一个全是0的数组
    函数ones创建一个全1的数组
    函数empty创建一个内容随机并且依赖于内存状态的数组。默认创建的数组类型(dtype)都是float64
    函数arange()类似 python 的 range() ，创建一个一维 ndarray 数组
    函数是 ndarray 的子类，只能生成 2 维的矩阵
"""

########## Numpy
import numpy as np

# 创建3行5列的ndarray对象
arr = np.arange(15).reshape((3, 5))
print(arr)
print(f'数组的维度: {arr.shape}')  # (3, 5)   3个元素(一维数组), 每个元素(一维数组)又有5个元素(值)
print(f'数组轴的个数: {arr.ndim}')  # 几维数组, 轴就是几,  2
print(f'数组元素类型: {arr.dtype}')  # int64
print(f'数组每个元素的占用字节数: {arr.itemsize}')  # 8
print(f'数组元素个数: {arr.size}')  # 15
print(f'数组类型: {type(arr)}')  # <class 'numpy.ndarray'>

########## ndarray
a = np.array([2, 3, 4])
print('数组a元素类型: ', a)
print('数组a类型:', a.dtype)
b = np.array([1.2, 3.5, 5.1])
print('数组b元素类型: ', b)
print('数组b类型:', b.dtype)

##########
zero1 = np.zeros((3, 4))    # 3个一维数组, 每个长度为: 4
print('数组zero1: ', zero1)
ones1 = np.ones((2, 3, 4))  # 2个二维数组, 每个二维数组有3个一维数组, 每个一维数组有4个元素1, 整体放入1个数组中
print('数组one1: ', ones1)
empty1 = np.empty((2, 3))
print('数组empty1: ', empty1)
print(zero1.dtype, ones1.dtype, empty1.dtype)
np_arange = np.arange(10, 20, 5,dtype=int)   # 起始, 结束, 步长, 类型
print("arange创建np_arange:", np_arange)
print("arange创建np_arange的元素类型:", np_arange.dtype)
print("arange创建np_arange的类型:", type(np_arange))
x1 = np.asmatrix("1 2;3 4")
print(x1)
x2 = np.matrix("1,2;3,4")
print(x2)
x3 = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
print(x3)

########## 创建随机数矩阵
import numpy as np

# 生成指定维度大小(3行4列)的随机多维浮点型数据(二维), rand固定区间0.0 ~ 1.0
arr = np.random.rand(3, 4)
print(arr)
print(type(arr))

# 生成指定维度大小(3行4列)的随机多维整型数据(二维), randint()可指定区间(-1, 5)
arr = np.random.randint(-1, 5, size=(3, 4))
print(arr)
print(type(arr))

#生成指定维度大小(3行4列)的随机多维浮点型数据(二维), uniform()可以指定区间(-1, 5)产生-1到5之间均匀分布的样本值
arr = np.random.uniform(-1, 5, size=(3, 4))
print(arr)
print(type(arr))
