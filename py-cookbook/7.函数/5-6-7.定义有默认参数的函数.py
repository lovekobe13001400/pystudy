def spam(a,b=42):
    print(a,b)

spam(1)
spam(1,2)


#如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来，可以像下面这样写：

#因为不传值
_no_value = object()
def spam(a,b=_no_value):
    if b is _no_value:
        print('no value come in ')

spam(1,None)
spam(1)

#匿名函数

add = lambda x,y:x+y
add(2,3)

#运用
names = ['a','david','briam jones']
b = sorted(names,key=lambda name:name.split()[-1].lower())
print(b)


names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']

for i in names:
    print(i.split()[-1])


#匿名函数捕获变量值

x = 10
a = lambda y:x+y

x = 20
b = lambda y:x+y
#这其中的奥妙在于lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。 因此，在调用这个lambda表达式的时候，x的值是执行时的值。
a(10) #30
b(10) #30

#x是在运行时绑定的
x = 10
a(10)
x = 20
a(10)

#如果要定义时绑定，可以设置默认值
x1 = 10
a1 = lambda y,x1 = x1:x1+y

x2 = 20

a2 = lambda y,x2 = x2:x2+y

a1(10)
a2(10)

#运用

#匿名函数函数列表，传x,默认值为n
funcs = [lambda x,n=n:x+n for n in range(5)]

for f in funcs:
    print(f(0))