def count(n):
    while True:
        yield  n
        n += 1

c = count(0)
#迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引
# c[10:20]

import itertools
for x in itertools.islice(c,10,20):
    print(x)

for i in c:
    print(i)


