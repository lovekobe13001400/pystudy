def apply_async(func,args,*,callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got:',result)


def add(x,y):
    return x+y

apply_async(add,(2,3),callback=print_result)

#为了让回调函数访问外部信息

#方法1：绑定方法来代替一个简单函数

class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self,result):
        self.sequence += 1
        print('[{}] Got :{}'.format(self.sequence,result))


r = ResultHandler()
apply_async(add,(2,3),callback=r.handler)
#sequence就能累加了
apply_async(add,(2,3),callback=r.handler)

#方法2：用闭包捕获状态值

def make_handler():
    sequence = 0
    def handler(result):
        #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        nonlocal sequence
        sequence += 1
        print('[{} Got:[]]'.format(sequence,result))
    return handler

handler = make_handler()
apply_async(add,(2,3),callback=handler)


#还有另外一个更高级的方法，可以使用协程来完成同样的事情：

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got:{}'.format(sequence,result))

#对于协程，你需要使用它的 send() 方法作为回调函数

handler = make_handler()
next(handler)
apply_async(add,(2,3),callback=handler.send)


