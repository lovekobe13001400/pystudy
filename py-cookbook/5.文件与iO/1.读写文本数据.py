#rt模式下，python在读取文本时会自动把\r\n转换成\n.

with open('../file.txt','rt') as f:
    for line in f:
        print(line.strip())

    #读取所有行
    lines = f.readlines()
    print(lines)

#覆盖
with open('../file.txt','wt') as f:
    f.write('aaa')
    f.write('bbb')

#添加
with open('../file.txt','at') as f:
    f.write('hello world')

#print到文件中

with open('../file.txt','wt') as f:
    print('write wt',file=f)

