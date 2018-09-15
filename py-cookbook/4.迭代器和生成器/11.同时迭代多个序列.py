x_list = [1,2,3,4]
y_lsit = [5,10,15,20]

#迭代多个序列
# for x,y in zip(x_list,y_lsit):
#     print(x,y)



#zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中x来自a，y来自b。 一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。

x_list = [1,2,3,4]
y_lsit = [5,10]
#结果只有 1 5   2 10
for x,y in zip(x_list,y_lsit):
    print(x,y)


#如果不全也想要

from itertools import zip_longest
for i in zip_longest(x_list,y_lsit):
    print(i)


#结合dic变成字典

keys = ['name','age']
values = ['jack',100]
person = dict(zip(keys,values))

#最后强调一点就是， zip() 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 list() 函数。比如：

#存字典也一样
print(person)
