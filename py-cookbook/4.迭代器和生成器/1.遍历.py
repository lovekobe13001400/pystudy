

with open('../file.txt') as f:
    #会有空格
    for i in f:
        #这样就没有空行了

        #发现打印输出有空行，这是因为文本已经带了一个 '\n' 了，print  默认也是 '\n'，所以就换了两行。
        #去除空行
        if i.strip()=='python':
            print('yes\r\n')
            break
        print(i,end="")


with open('../file.txt') as f:
    #会有空格
    while True:
        line = next(f,None)
        if line is None:
            break
        print(line,end='')


#底层迭代机制

items = [1,2,3]

it = iter(items)

next(it)
next(it)
next(it)

##StopIteration
##使用 next() 函数并在代码中捕获 StopIteration
next(it)

