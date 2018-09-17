#你想将一个多层嵌套的序列展开成一个单层列表
from collections import Iterable

def flatten(items,igore_types=(str,bytes)):
    for x in items:
        #检查是否可迭代 并且不再忽略的类型里面
        if isinstance(x,Iterable) and not isinstance(x,igore_types):
            #yield from 语句的递归生成器
            #为了让生成器（带yield函数），能简易的在其他函数中直接调用，就产生了yield from。
            yield from flatten(x)
        else:
            yield x


items = [1,2,[3,4,[5,6],7],8]

for x in flatten(items):
    print(x)


