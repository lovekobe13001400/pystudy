import pandas as pd
drinks = pd.read_csv('./tsv/drinks.csv')
#1.看下结构
# print(drinks.head())

#2.对每个continent 分组 求每个分组的beer_servings的品均值
# print(drinks.groupby('continent').beer_servings.mean())

#3.对每个continent 分组 求每个分组的wine_servings的各种信息
# print(drinks.groupby('continent').wine_servings.describe())

#3.对每个continent 分组 求每个分组的所有其他的各种平均值
# print(drinks.groupby('continent').mean())

#4.中位数
# print(drinks.groupby('continent').median())
#5.最大值，最小值得集合
print(drinks.groupby('continent').wine_servings.agg(['min','max','mean']))