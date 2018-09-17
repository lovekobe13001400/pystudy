from functools import partial

RECORD_SIZE = 32

#你想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代。
with open('../file.txt','rb') as f:
    records = iter(partial(f.read,RECORD_SIZE),b'')
    for r in records:
        #r就是数据块
        print(r)


