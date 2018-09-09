#1.
p = (4,5)
x,y = p
x,y
#2.有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况 Python 并没有提供特殊的语法。 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
a,_,b,_ = (1,2,3,4)
a,b

#3.如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
a,*middle,b = (1,2)
a,b,middle
#4.另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。 你可以像下面这样分解这些记录：
name,email,*phone_numbers = ('jack','qq.com','1234')
phone_numbers

name,email,*phone_numbers = ('jack','qq.com','1234','119','110')
phone_numbers