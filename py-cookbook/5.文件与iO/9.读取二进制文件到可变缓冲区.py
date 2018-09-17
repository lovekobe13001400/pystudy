import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf

with open('../file.txt','wb') as f:
    f.write(b'hello world')

buf = read_into_buffer('../file.txt') # bytearray(b'hello world')

#注意是二进制文件哦
buf

#再写入新的文件
with open('../new_file.txt','wb') as f:
    f.write(buf)

#

record_size = 32
#
# buf = bytearray(record_size)
# with open('../file.txt','rb') as f:
#     while True:
#         n = f.readinto(buf)
#         if n < record_size:
#             break


#memoryview 对缓冲区进行操作
buf = bytearray(b'hello world')
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2[:])

