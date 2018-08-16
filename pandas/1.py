import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#用一个包含值的序列创建一个Series，pandas会创建一个默认的整数索引
s = pd.Series([1,3,4,np.nan,6,8])
#print(s)
#用numpy数值创建一个带有datetime索引和列标签的数据框
dates = pd.date_range('2013-01-01',periods=6)
#print(dates)

'''
numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。 
numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。 
'''
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#print(df)

#用包含对象的字典创建一个数据框，该方法与创建Series的方法相似。
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
#查看数据
# print(df.head(3))
# print(df.tail(4))
# print(df.index)
# print(df.columns)

#转置数据
#print(df.T)
#通过轴来分类你的数据（相当于排序，axis=1可以理解为分类列名，=0则为索引名）
#new_df = df.sort_index(axis=0,ascending=False)

#通过值来分类
new_df = df.sort_values(by='B',ascending=False)
#print(new_df)
#print(new_df['B'])

#切片获取数据
#print(df[0:3])


#用标签获取数据
# print(df.loc[dates[0]])
#
# #在多个轴上通过标签来选取数据
# print(df.loc[:,['A','B']])
# print(df.loc[dates[0]:dates[1],['A','B']])
# #仅仅获取标量值的方法
# print(df.loc[dates[0],'A'])

#通过适合的整数来代表位置进行索引
#print(df.iloc[3])

#切片
# print(df.iloc[3:5,0:2])
#
# print(df.iloc[[1,2,4],[1,2]])
df.iloc[1:3,:]
df.iloc[:,1:3]
#显式索引数据值
df.iloc[2,3]
df.iat[1,1]

#列值>0
df[df.A>0]

#使用isin来过滤诗句

# df2 = df.copy()
# df2['E'] = ['one', 'one','two','three','four','three']
# new_df2 = df2[df2['E'].isin(['two','four'])]
# print(new_df2)
#在安插新的列时通过索引值自动排列
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
#print(s1)
#
# #r通过标签安插值
# df.at[dates[0],'A'] = 0
# #通过位置暗插值
# df.iat[0,1] = 0
#通过分配numpys数组来安插新的列

# df.loc[:,'D'] = np.array([1] * len(df))
# arr = [1] * 6
# df2 = df.copy()
# print(df2)
# #大于0的值 取反
# df2[df2 > 0] = -df2
# print(df2)
#
#print(df)
# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# df1.loc[dates[0]:dates[1],'E'] = 1
# df2 = df1.dropna(how='any')
#
# #替换缺失值
# print(df2)
# print(df)
# print(df.mean(1))
# print(df.apply(np.cumsum))
# #对数据进行函数的运用
# print(df.apply(lambda x: x.max() - x.min()))

# #统计词的频数
# s = pd.Series(np.random.randint(0, 7, size=10))
# print(s)
# print(s.value_counts())
#
# #字符串操作
# s = pd.Series(['A','B'])
# s1 = s.str.lower()
# print(s1)

'''
pandas提供了不同的工具为了简便地用不同的方式来对索引设置逻辑和相关的代数功能结合Series，
DataFrame和Panel对象，例如join/merge-type操作
'''
# df = pd.DataFrame(np.random.randn(10,4))
# pieces = [df[:3],df[3:7],df[7:]]
# print(pieces)
# print(pd.concat(pieces))
#
# ##Join
# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# all = pd.merge(left,right,on='key')
# print(all)
#
# #对数据库附加行
# df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
# s = df.iloc[3]
# print(df.append(s,ignore_index=True))
#
# df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
#                         'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
#                         'C' : np.random.randn(8),
#                         'D' : np.random.randn(8)})
# print(df)
# print(df.groupby('A').sum())
# print(df.groupby(['A','B']).sum())

#重塑
#有堆叠
# tuples = list(zip(*[
#     ['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],
#     ['one', 'two', 'one',  'two', 'one', 'two', 'one', 'two']
# ]))
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# print(index)
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# print(df)
# stacked = df2.stack()
# print(stacked)


#画图
import matplotlib.pyplot as plt
import numpy as np
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()


