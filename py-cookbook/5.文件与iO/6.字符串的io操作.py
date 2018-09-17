
#使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据
import io

s = io.StringIO()

s.write('Hello World\n')

#往s里面写

print('This is a test',file=s)

#s.getvalue()#'Hello World\nThis is a test\n'

s = io.StringIO('Hello\nWorld\n')
s.getvalue()
s.read(6) #Hello\b
#读6个字符
s.read(6) #World\n

#如果是中文
s = io.StringIO('你好\n世界\n')
s.read(2)

