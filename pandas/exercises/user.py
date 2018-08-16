import pandas as pd

users = pd.read_table('./table/user.table',sep='|',index_col='user_id')

#1.有多少种职业
occupation_num = users.occupation.nunique()
#等同于
occupation_num = users.occupation.value_counts().count()
#最频繁的职业
occupation_regalur = users.occupation.value_counts().head(6)
#各种统计信息
#print(users.describe(include = "all"))
#获取年龄的平均值
avg_age = users.age.mean()
print(avg_age)