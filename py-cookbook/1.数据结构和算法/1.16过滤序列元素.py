#生成器能：省内存
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = (n for n in mylist if n>0)
for i in pos:
    print(i)

#复杂过滤
mylist = [1, 4, -5, 10, -7, 2, 3, -1,'N/A']

def is_int(val):
    if type(val) is int:
        return True
    else:
        return False
#filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例那样使用 list() 去转换。
ivals = list(filter(is_int,mylist))
print(ivals)

#另外一个值得关注的过滤工具就是 itertools.compress() ， 它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
#  然后输出 iterable 对象中对应选择器为 True 的元素。 当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的。 比如，假如现在你有下面两列数据：

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]


addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
#counts对应了addres每个内容的数量
from itertools import compress
#[False, False, True, False, False, True, True, False]
more5 = [n>5 for n in counts]

list(compress(addresses,more5))




