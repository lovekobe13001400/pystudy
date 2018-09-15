my_list = ['a','b','c']
#enumerate() 函数返回的是一个 enumerate 对象实例， 它是一个迭代器，返回连续的包含一个计数和一个值的元组
for idx,val in enumerate(my_list):
    print(idx,val)


for tuple_tmp in enumerate(my_list):
    #(0, 'a') 为元祖
    print(tuple_tmp)

def parse_data(filename):
    with open(filename,'rt') as f:
       for lineno,line in enumerate(f,1):
           fields = line.split()
           try:
               count = int(fields)
           except Exception as e:
               #提示错误
               print('Line{}:Parse error:{}'.format(lineno,e))

# parse_data('../file.txt')



#如果你想将一个文件中出现的单词映射到它出现的行号上去
#defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，这个默认值是什么呢，下面会说
from collections import defaultdict
word_summary = defaultdict(list)
word_summary2 = defaultdict(list)
with open('../file.txt','r') as f:
    lines = f.readlines()
#lines : ['apython\n', 'bpython\n', 'cpython\n', 'dpyton\n', 'dfe\n', 'pyton\n', 'python\n', 'ee']
for idx,line in enumerate(lines):
    words = [x.strip().upper() for x in line.split()]
    for word in words:
        word_summary[word] = idx
        word_summary2[word].append(idx)
#{'PYTHON': 7, 'APYTHON': 1, 'BPYTHON': 2, 'CPYTHON': 3, 'DPYTON': 4, 'DFE': 5, 'PYTON': 6, 'EE': 8})
print(word_summary)
#{'PYTHON': [0, 7], 'APYTHON': [1], 'BPYTHON': [2], 'CPYTHON': [3], 'DPYTON': [4], 'DFE': [5], 'PYTON': [6], 'EE': [8]})
print(word_summary2)