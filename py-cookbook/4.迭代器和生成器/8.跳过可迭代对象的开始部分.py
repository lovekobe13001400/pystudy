from itertools import islice,dropwhile

items = ['a','b','c',1,4,10,15]

#起步从下标3开始
# for x in islice(items,3,None):
#     print(x)


#如果items比较乱，

items = [1,2,'a','b',2,3]
#1,2可去除，a,b开始就一直输出了
#只跳过可迭代对象的开始部分
for x in dropwhile(lambda x:type(x) is int,items):
    print(x)


