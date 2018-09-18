import pandas as pd

users = pd.read_table('./table/user.table',sep='|',index_col='user_id')

#1.有多少种职业
occupation_num = users.occupation.nunique()
#等同于
occupation_num = users.occupation.value_counts().count()
#每个职业的数量
occupation_num = users.occupation.value_counts()
#最频繁的职业
occupation_regalur = users.occupation.value_counts().head(6)
#各种统计信息
#print(users.describe(include = "all"))
#获取年龄的平均值
avg_age = users.age.mean()
#每个职业的平均值
occupation_avg_age = users.groupby('occupation').age.mean()

#每个职业男性的比例
def gender2numeric(x):
    if x == 'M':
        return  1
    else:
        return 0

users['gender_n'] = users['gender'].apply(gender2numeric)
#每个职业男性的数量
occupation_male_num = users.groupby('occupation').gender_n.sum()
#每个职业的数量
every_occupation_num = users.occupation.value_counts()
#每个职业 male的比例
rate = occupation_male_num / every_occupation_num * 100
rate = rate.sort_values(ascending=False)
#每个职业的性别的年龄平均值
# 统计每个gender的数量 create a data frame and apply count to gender
gender_ocup = users.groupby(['occupation','gender']).agg({'gender':'count'})
# 统计每个职业的数量 create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count')
# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count,level='occupation')*100
#行全部 列取gender
rate = occup_gender.loc[:,'gender']
print(rate)



