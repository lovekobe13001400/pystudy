import gzip
import zipfile
with gzip.open('../aaa.gz','rt',encoding='utf8') as f:
    #文件列表(包括文件里面的内容)
    print(f.read())


    #写

with gzip.open('../aaa.gz','wt') as f:
    #写文本
    f.write('../b.txt')
    #文件
    # with open('../b.txt','w') as ff:
    #     f.write(ff)







