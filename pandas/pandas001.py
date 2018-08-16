import numpy as np
import pandas as pd

#不关注索引 data=字典
df1 = pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[5,6,7]})

#二维数组 + index + columns
data_list = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#生成随机数
data_list = np.random.randint(low=0, high=10, size=(4, 4))
#符合正态分布的随机数
data_list = np.random.randn(4,4)


index_list = ['tom','jack','amy','rose']
columns = list("ABCD")
#dtype=np.int64 对数据类型进行处理
df2 = pd.DataFrame(data_list,index=index_list,columns=columns,dtype=np.int64)
df2 = pd.DataFrame(data_list,index=index_list,columns=columns)

#loc 通过标签或者布尔数组访问
#iloc 通过位置
res1 = df1.loc[[0,1,2]]
res1 = df2.loc[['tom','jack']]
res2 = df1.iloc[0,1]
#if then if行 then 列

res2 = df2.loc[['tom','jack'],['A','B']]
#作用1列:A列大于-1，B列进行修改
df2.loc[df2.A>-1,'B'] = 1

#作用2列
df2.loc[df2.A>-1,['B','C']] = 1

#设置一个面具
#print(df2)
# df_mask = pd.DataFrame({"A":[True]*4,"B":[False]*4,"C":[True,False]*2,"D":[True]*4})
# print(df_mask)
# df2_new = df2.where(df_mask,110)
# print(df2_new)
#print(df2.iloc[1:3,2:4])
df = pd.DataFrame({'AAA' : [1,2,1,3], 'BBB' : [1,1,2,2], 'CCC' : [2,1,3,1]});
#列索引
source_cols = df.columns
#新的列索引
new_cols = [str(x) + "_cat" for x in source_cols]
#
categories = {1 : 'Alpha', 2 : 'Beta', 3 : 'Charlie' }
#categories.get 获取所有
#print(categories.get)
# df[new_cols] = df[source_cols].applymap(categories.get)
# print(df[new_cols])
# print(df)

# df = pd.DataFrame( {'AAA' : [1,1,1,2,2,2,3,3], 'BBB' : [2,1,3,4,5,1,2,3],'CCC' : [2,1,9,4,5,9,9,3]});
# print(df.groupby("AAA")["BBB"].idxmin)
# new_dif = df.loc[df.groupby("AAA")["BBB"].idxmin]
# print(new_dif)
# df = pd.DataFrame({'month': [1, 4, 7, 10],'year': [2012, 2014, 2013, 2014],'sale':[55, 40, 84, 31]})
# nwe_df = df.set_index('year')
# print(nwe_df)
# s = pd.Series([1, 2, 3, 4])
# s = pd.Series([1, 2, 3, 4], name='foo', index=pd.Index(['a', 'b', 'c', 'd']))
# print(s)
# print(s.reset_index(name='gg'))
coords = [('AA','one'),('AA','six'),('BB','one'),('BB','two'),('BB','six')]
index = pd.MultiIndex.from_tuples(coords)
#print(index)


df = pd.DataFrame({'A' : [1, 1, 2, 2], 'B' : [1, -1, 1, 2]})
print(df)
gb = df.groupby('A')
print(gb)
def replace(g):
    mask = g < 0
    g.loc[mask] = g[~mask].mean()
    return g

# print(gb.transform(replace))

df = pd.DataFrame({'类别':['水果','水果','水果','蔬菜','蔬菜','肉类','肉类'],
                '产地':['美国','中国','中国','中国','新西兰','新西兰','美国'],
                '水果':['苹果','梨','草莓','番茄','黄瓜','羊肉','牛肉'],
               '数量':[5,5,9,3,2,10,8],
               '价格':[5,5,10,3,3,13,20]})
# print(df)
# print(df.groupby('类别').transform(np.mean))

df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','MN','ON'],'City' : ['Toronto','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],'Sales' : [13,6,16,8,4,3,1]})
print(df)
table = pd.pivot_table(df,values=['Sales'],index=['Province'],columns=['City'],aggfunc=np.sum,margins=True)
print(table('City'))

