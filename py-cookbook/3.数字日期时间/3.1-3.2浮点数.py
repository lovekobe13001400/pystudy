
#1.四舍五入

round(1.33345,2)

#round 函数返回离它最近的偶数。 也就是说，对1.5或者2.5的舍入运算都会得到2。

round(1.5)
round(2.5)
#结果都为2

#传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面
round(12345,-1) #12340
round(12345,-2) #12300

##2.精确浮点数运算
a = 4.2
b = 2.1
a+b #6.300000000000001
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
a + b
#有什么用？？decimal模块 金融领域
'''
>>> from decimal import localcontext
>>> a = Decimal('1.3')
>>> b = Decimal('1.7')
>>> print(a / b)
0.7647058823529411764705882353
>>> with localcontext() as ctx:
...     ctx.prec = 3
...     print(a / b)
...
0.765
>>> with localcontext() as ctx:
...     ctx.prec = 50
...     print(a / b)
...
0.76470588235294117647058823529411764705882352941176
>>>
'''