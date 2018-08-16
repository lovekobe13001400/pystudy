#re模块
import re
str = '010-12345'
pattern = r'\d{3}-\d{3,8}'
result = re.match(pattern,str)
#匹配成功返回math对象，失败返回none
# print(result)
# print(re.split(r'\s+','a b c   dd'))
# print(re.split(r'[\s\,]+','a  ,b   ,c'))
# print(re.split(r'[\s\,]+','a  ,,,b   ,c'))
# print(re.split(r'[\s]+,+','a  ,,,b   ,c'))
# print(re.split(r'[ab]+','cabaabbbc'))
# print(re.split(r'a+b+','cabaaabbbc'))
# print(re.split(r'[a+b+]','cabaaabbbc'))
#d逗号分隔的整数（人民币）
# pattern = r'\b[0-9]{1,3}(,[0-9]{3})*\b'
# m = re.findall(pattern,'1,234,4,555')
#print(m)
pattern = r'\+?(\d+|\d+\.\d+|)|\.\d+'
str = 'a++1.11b-12.12,22d2112.1144.11a11+.1'
print(re.findall(pattern,str))