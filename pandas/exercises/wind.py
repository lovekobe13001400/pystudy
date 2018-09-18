import pandas as pd
from datetime import datetime
from datetime import date
#parse_dates = [0,1,2]
data = pd.read_csv('./tsv/wind.csv',sep = "\s+", parse_dates = [[0,1,2]])
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    year,month,day = int(year), int(x.month), int(x.day)
    return date(year,month,day)
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])
data = data.set_index('Yr_Mo_Dy')

##为空数量
num = data.notnull().sum()
num_num = data.isnull().sum()

#na 填0
data = data.fillna(0)

#
m1 = data.fillna(0).values.flatten().mean()
m2 = data.fillna(0).values.mean()
print(m2,m1)

#获取1月的数据


# print(data.head())
d = data.loc[data.index.month == 1].mean()
# print(d)

#按年分组取品均值
d1 = data.groupby(data.index.to_period('A')).mean()
d2 = data.groupby(data.index.to_period('Y')).mean()
data.groupby(data.index.to_period('M')).mean()
print(d1)
print(d2)
