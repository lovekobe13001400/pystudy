from collections import defaultdict
#字典映射多个值
#defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。比如：
d_list = defaultdict(list)
d_list['a'].append(1)
d_list['a'].append(2)
d_list['b'].append(4)
print(d_list)
d_set = defaultdict(set)
d_set['a'].add(1)
d_set['a'].add(2)
d_set['b'].add(4)
print(d_set)

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

#不会报错，或者返回特别的内容
dd = defaultdict(lambda: 'N/A')
dd2 = defaultdict(lambda: 'love you1')
dd['key1'] = 'abc'
print(dd['key2'])
print(dd2['key2'])


#字典排序
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。 所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候（比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去）， 那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
from collections import OrderedDict
#python3.6是有序的



#字典运算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#values在前
prices_zip_list = list(zip(prices.values(), prices.keys()))
# prices_zip_list = list(zip(prices.keys(), prices.values()))
print(prices_zip_list)
print(min(prices_zip_list))
print(max(prices_zip_list))

#如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值。比如：
print(min(prices),max(prices))
#这个结果并不是你想要的，因为你想要在字典的值集合上执行这些计算。 或许你会尝试着使用字典的 values() 方法来解决这个问题：
print(min(prices.values()))# Returns 10.75
print(max(prices.values())) # Returns 612.78

#不幸的是，通常这个结果同样也不是你想要的。 你可能还想要知道对应的键的信息（比如那种股票价格是最低的？）。
#你可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息。比如：
#按照value取最小值，返回键值
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

# 需要注意的是在计算操作中使用到了 (值，键) 对。当多个实体拥有相同的值的时候，键会决定返回结果。 比如，在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回：


#1.9查找两字典的相同点
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}