"""
变量介绍
    概念
        变量是存储数据的容器
        变量在程序运行的过程中是可以发生改变的
        变量存储的数据是临时的
    定义
        变量名 = 变量值
    数据类型
        int  整型
        float  浮点型
        bool  布尔值
        str  字符型
        NoneType  None
"""
a: int | None = 100
print(a)
print(type(a))
a = None
print(a)
print(type(a))
