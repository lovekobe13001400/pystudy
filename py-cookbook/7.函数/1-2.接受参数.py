
#接受任意数量的位置参数
def avg(name,*friends):
    str = name
    for i in friends:
        str += 'friend is %s and'%i
    return str

print(avg('jack','tom','mike'))


#接受任意数量的关键字参数，使用一个以**开头的参数

#friends是一个包含所有被传入进来的关键字参数的字典。
#** 字典
def person(name,age,**friends):
    print(name,age,friends)

person('tom',10,lover='lose',eat='apple')


def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict

anyargs('tom',10,lover='amy')

#语法错误：positional argument follows keyword argument
# anyargs('tom',10,lover='amy',101)


#只接受关键字参数的函数


#*前面是位置，*后面是关键字
def recv(maxsize,*,block):
    'receives a message'
    pass

#TypeError
# recv(1024,True)


recv(1024,block=True)


def minimum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

