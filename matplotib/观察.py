#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from mysql.MysqlHelper import *
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#函数返回一个figure图像和一个子图ax的array列表。
# fig, ax = plt.subplots()
#添加一个轴left, bottom, width, height
plt.subplots_adjust(left=0.25, bottom=0.25)

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

line_price,= plt.plot(x,price,color='red')
line_money,= plt.plot(x,money,color='purple')
axcolor = 'lightgoldenrodyellow'
#添加一个轴left, bottom, width, height
axfreq = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

#滑块：min max 默认值 步长
sfreq = Slider(axfreq, '周几', 0, 5, valinit=1, valstep=1)
#
samp = Slider(axamp, '股票', 1, 10.0, valinit=1,valstep=1)


def update(val):
    # amp = samp.val
    freq = sfreq.val

    line_price.set_ydata(money)
    line_money.set_ydata(price)

    fig.canvas.draw_idle()


sfreq.on_changed(update)
# samp.on_changed(update)

# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


# def reset(event):
#     sfreq.reset()
#     samp.reset()
# button.on_clicked(reset)

# rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


# def colorfunc(label):
#     l.set_color(label)
#     fig.canvas.draw_idle()
# radio.on_clicked(colorfunc)

plt.show()