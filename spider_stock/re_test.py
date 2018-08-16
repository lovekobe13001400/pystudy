import re
pattern = re.compile('\d+')
'''
match 方法：从起始位置开始查找，一次匹配
search 方法：从任何位置开始查找，一次匹配
findall 方法：全部匹配，返回列表
finditer 方法：全部匹配，返回迭代器
split 方法：分割字符串，返回列表
sub 方法：替换
'''
#match测试
m1 = pattern.match('abc1234dd33dd')
print(m1)#none

m2 = pattern.match('abc1234dd33dd',3)
print(m2)#返回一个match对象

print(m2.group())
print(m2.start())
print(m2.end())
print(m2.span())

#search测试
pattern2 = re.compile('\d+')
s1 = pattern2.search('abc1234dd33dd')
print(s1)
print(s1.group(0))

#测试findall
pattern3 = re.compile(('\d+'))
f1 = pattern3.findall('abc1234dd33dd')
print(f1)

#测试finditer
pattern4 = re.compile('\d+')
f2 = pattern4.finditer('abc1234dd33dd')
print('finditer')
for son in f2:
    print(son.group())
#测试split方法（空白字符，逗号，分号，分割）
p = re.compile(r'[\s\,\;]+')
print(p.split('a,b;;c d'))

#测试sub方法
su = re.compile('(\w+) (\w+)')
s = 'hello 123,hello 456'
#hello XXX替换为hello world
print(su.sub('hello world',s))
#只替换一次
print(su.sub('hello world',s,1))

#匹配中文
title = '你好，中国'
pattern = re.compile('中国')
result = pattern.findall(title)
print(result)
#p匹配所有中文
title = u'你好，hello,世界'
pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print(result)


