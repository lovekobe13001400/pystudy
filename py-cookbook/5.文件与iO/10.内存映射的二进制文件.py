import os
import mmap

#使用 mmap 模块来内存映射文件
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('../file.txt','wb') as f:
    f.seek(size-1)
    f.write(b'\x00')


#下面是一个利用 memory_map() 函数类内存映射文件内容的例子：

m = memory_map('..//file.txt')
print(len(m))
#因为内存映射文件
m[0:11] = b'Hello World'
m.close()


with open('../file.txt') as f:
    print(f.read(11))

