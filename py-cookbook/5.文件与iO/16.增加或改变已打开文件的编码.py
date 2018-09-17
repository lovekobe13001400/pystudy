import urllib.request
import io

# u = urllib.request.urlopen('http://www.python.org')
#
# #如果你想给一个以二进制模式打开的文件添加Unicode编码/解码方式
# f = io.TextIOWrapper(u,encoding='utf-8')
#
# text = f.read()
#
# print(text)


#I/O系统由一系列的层次构建而成。你可以试着运行下面这个操作一个文本文件的例子来查看这种层次：


f = open('./file.txt','w')

#<_io.TextIOWrapper name='./file.txt' mode='w' encoding='cp936'>
print(f)

#_io.FileIO name='./file.txt' mode='wb' closefd=True>
print(f.buffer.raw)

#io.TextIOWrapper 是一个编码和解码Unicode的文本处理层


#将字节写入文本文件








