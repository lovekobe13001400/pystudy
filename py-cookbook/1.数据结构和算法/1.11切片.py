record = '....................100 .......513.25 ..........'
SHARES = slice(20,23)
PRICE = slice(31,37)
#切片1,推荐使用这个
cost = int(record[SHARES]) * float(record[PRICE])

#切片2(其实也挺好理解的)
print(int(record[20:23])*float(record[31:37]))

#不知道用来干嘛
# a = slice(5,50,2)
# s = 'HelloWorld'
# l = a.indices((len(s)))
# print(l)



