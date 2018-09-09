from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
Subscriber = namedtuple('Subscriber2',['addr','joined'])
#Subscriber2 可以理解类实例，但是又可以跟元组类型一样可交换，支持所有的普通元组操作，比如索引和解压。 比如：
sub = Subscriber('jonesy@qq.com','2019-01-01')
a,b = sub
print(a,b)

'''
命名元组的一个主要用途是将你的代码从下标操作中解脱出来。 因此，如果你从数据库调用中返回了一个很大的元组列表，
通过下标去操作其中的元素， 当你在表中添加了新的列的时候你的代码可能就会出错了。但是如果你使用了命名元组，那么就不会有这样的顾虑。
'''
Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        #rec是一个元组：
        #  *rec拆，跟stock对应
        #* 的作用其实就是把序列 args 中的每个元素，当作位置参数传进去。比如上面这个代码，如果 args 等于 (1,2,3)
        s = Stock(*rec)
        print(s)
        total += s.shares * s.price
    return total

records = [('a',10,10),('b',20,20)]
print(compute_cost(records))


#元组用来当字典，省内存，但是不可修改
s = Stock('ACME',100,123.45)

#如果你真的需要改变属性的值，那么可以使用命名元组实例的 _replace() 方法， 它会创建一个全新的命名元组并将对应的字段用新的值取代。比如：
s2 = s._replace(shares=75)

#_replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，
#  它是一个非常方便的填充数据的方法。 你可以先创建一个包含缺省值的原型元组，然后使用 _replace() 方法创建新的值被更新过的实例。比如：

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print( dict_to_stock(a))
print( dict_to_stock(b))