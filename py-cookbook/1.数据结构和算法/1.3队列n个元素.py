from collections import deque
#下面的代码在多行上面做简单的文本匹配， 并返回匹配所在行的最后N行：
def search(lines,pattern,histroy=5):
    #生成一个队列
    previous_lines = deque(maxlen=histroy)

    for line in lines:
        #line是一行
        if pattern in line:
            #每一行，如果出现目标字符串，就返回当前line和最近N行（不包括自己）
            yield line,previous_lines
        previous_lines.append(line)


# my_que = deque(maxlen=3)
# my_que.append(1)
# my_que.append(2)
# my_que.append(3)
# #1会自动出队列
# my_que.append(4)
# print(my_que)
#
if __name__ == '__main__':
    with open(r'../file.txt') as f:
        #f是整个文件
        for line,previlines in search(f,'python',5):
            #最近N行,不包括当前行
            for pline in previlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)