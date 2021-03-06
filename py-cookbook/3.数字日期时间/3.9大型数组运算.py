x = [1,2,3,4]
y = [5,6,7,8]

#数组扩大2倍
x * 2

#数组合并
x + y

#引用numpy
import numpy as np

ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])

#里面的值乘以2
ax * 2
#里面的值加10
ax + 10

ax * ay

#要么只有一个，要么一一匹配
ax * [2]

#用处：
#用处：
def f(x):
    return 3*x**2 - 2*x + 7
f(ax)

#使用这些通用函数要比循环数组并使用 math 模块中的函数执行计算要快的多。 因此，只要有可能的话尽量选择 NumPy 的数组方案。

#numpy 索引功能
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a[1]

#获取列
