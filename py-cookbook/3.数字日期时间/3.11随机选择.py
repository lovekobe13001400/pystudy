import random

values = [1,2,3,4,5,6]
#随机获取一个
random.choice(values)

#为了提取出N个不同元素的样本用来做进一步的操作
random.sample(values,3)

#如果你仅仅只是想打乱序列中元素的顺序，可以使用 random.shuffle() ：
random.shuffle(values)
values

#
random.randint(0,10)

#为了生成0到1范围内均匀分布的浮点数，使用 random.random() ：

random.random()

#如果要获取N位随机位(二进制)的整数
random.getrandbits(200)