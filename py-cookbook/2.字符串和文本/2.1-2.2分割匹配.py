#
import re
#1.简单分割
str1 = 'a,b,c'
str1.split(',')

#2.正则分割
re.split(r',',str1)

#3.字符串开头和结尾匹配
a = 'hello word'
a.startswith('hello')#true
a.endswith('word') #true

#4.多结果匹配
filenames = ['a.py','a.java','c.php','d.py']

need_file = [file for file in filenames if file.endswith('.py') ]
#d多结果匹配，添加元组就行(如果是list，也得用tuple转成元组)
need_file = [file for file in filenames if file.endswith( ('java','php') ) ]
need_file

