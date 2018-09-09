parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)

#连接2

a = 'hello'
b = 'world'
a + b


#
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'
sample()

for i in sample():
    print(i)



#字符串的合并
s = '{name} has {n} messages'
s.format(name='jack',n=37)

#或者，如果要被替换的变量能在变量域中找到，
# 那么你可以结合使用 format_map() 和 vars() 。就像下面这样：

name = 'tom'
n = 30
s.format_map(vars())