"""
Numpy简介
    NumPy（Numerical Python）是Python数据分析必不可少的第三方库
    NumPy的出现一定程度上解决了Python运算性能不佳的问题，同时提供了更加精确的数据类型，使其具备了构造复杂数据类型的能力
    本身是由C语言开发，是个很基础的扩展，NumPy被Python其它科学计算包作为基础包，因此理解np的数据类型对python数据分析十分重要
    NumPy重在数值计算，主要用于多维数组（矩阵）处理的库。用来存储和处理大型矩阵，比Python自身的嵌套列表结构要高效的多
重要功能
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
        这是一个指示数组在每个维度上大小的整数元组。例如一个n排 m列的矩阵，它的shape属性将是(2,3),这个元组的长度显然是秩，即维度或者ndim属性。
"""


import numpy as np

arr = np