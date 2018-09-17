from tempfile import TemporaryFile

#通常来讲文本模式使用 w+t ，二进制模式使用 w+b
with TemporaryFile('w+t') as f:
    f.write('Hello world')
    f.write('Testing\n')
    f.seek(0)
    data = f.read()
    print(data)

from tempfile import NamedTemporaryFile

#如果目录要有名字
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)


