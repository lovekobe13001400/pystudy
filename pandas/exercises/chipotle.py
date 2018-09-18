import pandas as pd
import collections
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

url = './tsv/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')

#取前10个数据
top_10 =chipo.head(10)
# #有多少数量,chipo.shape = (4622,5)也就是多少行 多少列
# num = chipo.shape[0]
# #整个数据的所有信息,列索引 数据类型，数据内存大小
# #print(chipo.info())
# # print(chipo.columns)
# # print(chipo.index)
#
# #按照item_name排序
# c = chipo.groupby('item_name')
# c = c.sum()
# c = c.sort_values(['quantity'],ascending=False)
# #c就是groupby之后，统计好quantity的和，按照quantity降序排序
# #要统计某个菜品被下单的次数
# #1.按照choice_desciption排序 2.统计colums的和 3.quantity 降序排序
# c = chipo.groupby('choice_description').sum().sort_values(['quantity'],ascending=False)
# #计算总商品数
# order_goods_items = chipo.quantity.sum()
# #价格改变，去除$
# dollarizer = lambda x: float(x[1:-1])
# chipo.item_price = chipo.item_price.apply(dollarizer)
# #检查数据的类型
# chipo.item_price.dtype
# # print(chipo.item_price)
# #计算收入
# revenue  = np.round((chipo.item_price*chipo.quantity).sum(),2)
# #统计多少订单：
# order_num = chipo.order_id.value_counts().count()
# #每个订单的商品平均数量,统计每个订单quantity的和,item_price的和,对每个订单的数量和，价格和取平均
# mean_info = chipo.groupby('order_id').sum().mean()
#
# #统计有多少种商品被卖出
# #print(chipo.item_name.value_counts().count())
# #去重
# chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])
# #找到数量为1的记录
# chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
# #只取item_name和price
# price_item = chipo_one_prod[['item_name','item_price']]
# #按照price排序
# price_sort = price_item.sort_values('item_price',ascending=False)
#
# #筛选Canned Soda 数量>1
# s1 = chipo[(chipo.item_name=='Canned Soda')&(chipo.quantity>1)]

