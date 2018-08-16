import logging
import os
logging.basicConfig(level=logging.INFO)
from io import StringIO
class MyError(object):
    print('this is my error')
try:
    print('try..')
    r = 10/0
    print(r)
except ZeroDivisionError as e:
    print('except is',e)
    #logging.exception(e)
print('这里运行吗')

def mytest(n):
    if n==0:
        raise MyError()
#mytest(0)
# try:
#     mytest(0)
# except MyError as e:
#     print(e)

#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
def foo(n):
    pass
    #assert n!=0,"no er"
    #return 100/n
    #logging.info('错误信息')
foo(0)

with open('./io.txt','r',encoding='utf-8') as f:
    print(f.read())

#ff = StringIO()
ff = open('./io.txt','w',encoding='utf-8')
ff.write('bbbbbbb')
print(ff.write('hello'))

#操作文件和目录
#print(os.name)
#print(os.environ)
#查看当前目录的绝对路径
#print(os.path.abspath('.'))
#创建新目录
#new_dir = os.path.join('./','my_job')
#os.mkdir('./my_job')

#
dir = '/Users/michael/testdir/file.txt'
print(os.path.split(dir))

import json
d = dict(name='bob',age=20)
print(json.dumps(d))