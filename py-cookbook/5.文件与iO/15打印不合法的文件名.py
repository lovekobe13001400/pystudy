#当打印未知的文件名时，使用下面的方法可以避免这样的错误：

def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print('./noname.txt')
except UnicodeEncodeError:
    print(bad_filename('noname.txt'))

import os

for name in os.listdir( b'./'):
    print(name)