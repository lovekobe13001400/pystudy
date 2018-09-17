with open('../b.txt','wb') as f:
    f.write(b'hello world')

with open('../b.txt','rb') as f:
    print(f.readlines())



#只有文件不存在时才能写入

with open('../file.txt','w') as f:
    f.write('not exists')
#文件存在，写入会报错
# with open('../file.txt','x') as f:
#     f.write('use x not exits')

#文件不存在就可以正常插入
with open('../not.txt','x') as f:
    f.write('not exists')

