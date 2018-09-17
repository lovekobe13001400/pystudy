#如果你想让你的生成器暴露外部状态给用户， 别忘了你可以简单的将它实现为一个类，然后把生成器函数放到 __iter__() 方法中过去。比如：

from collections import deque


class linehistroy:
    def __init__(self,lines,histlen=3):
        self.lines = lines
        self.history = deque(maxlen = histlen)

    def __iter__(self):
        #numerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line

    def clear(self):
        self.history.clear()


with open('../file.txt') as f:
    lines = linehistroy(f)
    for line in lines:
        if 'python' in line:
            for lineno,hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')