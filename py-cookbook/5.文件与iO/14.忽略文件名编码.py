import sys
print(sys.getfilesystemencoding())

#奇葩文件名写入字符串
with open('jalape\xf1o.txt','w') as f:
    f.write('Spicy')

import os
print(os.listdir('./'))

print(os.listdir(b'.'))

#能把内容读取出来
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())