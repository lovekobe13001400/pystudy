import os

#你有一个对应于操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文件描述符， 你想将它包装成一个更高层的Python文件对象。
fd = os.open('../file.txt',os.O_WRONLY | os.O_CREAT)
print(fd)
f = open(fd,'wt')


## Turn into a proper file
f.write('hello world\n')
f.close()

