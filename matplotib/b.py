#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from mysql.MysqlHelper import *
from pylab import mpl
import datetime

from datetime import timedelta,date
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
####
now = datetime.datetime.now()
print(now)
db = MysqlHelper()
sql = "select * from tan_stock_record where sid='002415' and date='2018-07-18'";
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

#第一块
ax1 = plt.subplot2grid((9,9), (0,0), colspan=6,rowspan=6)
ax1.set_title("海康威视002415 price:-2.43% money:1.33%",fontsize=13)

plt.plot(x,price)
plt.plot(x,money)
#第二块
ax2 = plt.subplot2grid((9,9), (0,6), colspan=3,rowspan=3)
ax2.set_title("第二天k线")
plt.plot(x,price)
#第三块
ax3 = plt.subplot2grid((9,9), (3,6), colspan=3,rowspan=3)
ax3.text(0, 0, r'an equation: $E=mc^2$', fontsize=10)

axcolor = 'lightgoldenrodyellow'
#添加一个轴left, bottom, width, height
data_wave = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)

data_stock = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
data_day = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

print(now.weekday())
this_week_start = now - timedelta(days=now.weekday())
this_week_end = now + timedelta(days=6-now.weekday())
#print(this_week_start.strftime("%Y-%m-%d %H:%M",this_week_start),this_week_end)
print(date.strftime("%Y-%m-%d %H:%M",now))
#股票信息
def update(val):
    day = slider_day.val
    stock = slider_stock.val
    wave = slider_wave.val
    #根据wave,stock,day获取股票信息

    print(day,stock,wave)
def stock_info(wave,stock,day):
    pass
slider_wave = Slider(data_wave, '第几波', 0, 12, valinit=1, valstep=1)
slider_stock = Slider(data_stock, '股票', 0, 10, valinit=1, valstep=1)
slider_day = Slider(data_day, '第几天', 0, 5, valinit=1, valstep=1)
#绑定事件
slider_wave.on_changed(update)
slider_stock.on_changed(update)
slider_day.on_changed(update)
plt.show()