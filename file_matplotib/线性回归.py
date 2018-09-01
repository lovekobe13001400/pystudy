import numpy as np
import random
import math
import matplotlib.pyplot as plt

from mysql.MysqlHelper import *
def fitSLR(x,y):
    n=len(x)    #获取x的长度，x是list
    dinominator = 0#初始化分母
    numerator=0     #初始化分子
    for i in range(0,n):    #求b1
        numerator += (x[i]-np.mean(x))*(y[i]-np.mean(y))
        dinominator += (x[i]-np.mean(x))**2 #**表示平方


    b1 = numerator/float(dinominator)   #得出b1
    b0 = np.mean(y)/float(np.mean(x))   #得出b0

    return b0,b1
# y= b0+x*b1
def prefict(x,b0,b1):       #定义一个简单的线性方程
    return b0+x*b1
#获取股票
db = MysqlHelper()
sql = "select * from tan_stock_record where sid='002415' and date='2018-07-17'";
stock_info = db.get_all(sql)
price = []
money = []
x = []
xi = 0
price0 = 0
money0 = 0
for one_stock in stock_info:
    if xi==0:
        price0 = one_stock[3]
        money0 = one_stock[8] - one_stock[9] + one_stock[10] - one_stock[11]
        #第一个点没有资金进入这个点就不要了
        if money0 == 0:
            continue
        else:
            price.append(0)
            money.append(0)
    else:
        big_money = one_stock[8] - one_stock[9] + one_stock[10] - one_stock[11]



        #money0的多少倍
        price.append( 2000*(one_stock[3]-price0)/price0 )
        money.append((big_money-money0)/math.fabs(money0))
    xi += 1
    x.append(xi)
# for i in range(30):
#     x.append(i)
#     y.append(random.randint(1000,2000))
# print(y)
b0,b1=fitSLR(x, price)
price_k = b1
print(price_k)
bo,b1 = fitSLR(x,money)
money_k = b1
print(money_k)
plt.plot(x,price,color='red')
plt.plot(x,money,color='purple')
# 设置图例
plt.legend(["Price","Money"], loc="upper right")
plt.grid(True)
plt.show()

#print("y_predict:"+str(y_predict))

