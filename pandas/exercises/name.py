import numpy as py
import pandas as pd

baby_names = pd.read_csv('./tsv/name.csv')

# deletes Unnamed: 0# delet
del baby_names['Unnamed: 0']

# you don't want to sum the Year column, so you delete it# you d
del baby_names["Year"]
# deletes Unnamed: 0
del baby_names['Id']
print(baby_names.head())
#性别数量
fnum = baby_names['Gender'].value_counts()

#统计每个名字数量
names = baby_names.groupby('Name').sum()
names = names.sort_values("Count",ascending=False).head()

#数量最多的姓名
name_max = names.Count.idxmax()

#标准差
std = names.Count.std()
print(std)