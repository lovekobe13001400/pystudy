#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from mysql.MysqlHelper import *
from pylab import mpl
import datetime
from file_matplotib.help import *
from datetime import timedelta,date
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
####
now = datetime.datetime.now()

db = MysqlHelper()

price,money,x,sname,sid,pzdf_max,pzdf_min,money_max,money_min,next_pzdf_min,next_pzdf_max,next_price,money_all_half_slope,price_all_half_slope = stock_info(1,1,1)
#算每个点到起始点的斜率 斜率money - 斜率price 越大 越值得买


#第一块
ax1 = plt.subplot2grid((9,9), (0,0), colspan=6,rowspan=6)
title_str = "%s(%s)最高涨幅%s，最低涨幅%s,最大入单%s，最大出单%s"%(sname,sid,pzdf_max,pzdf_min,money_max,money_min)
ax1.set_title(title_str,fontsize=13)

line_price, = plt.plot(x,price,color='red')
line_money, = plt.plot(x,money,color='purple')
#第二块
ax2 = plt.subplot2grid((9,9), (0,6), colspan=3,rowspan=3)
ax2.set_title("第二天k线,最高涨幅%s 最低涨幅%s"%(next_pzdf_max,next_pzdf_min))
line_price_next, = plt.plot(x,next_price)
#第三块
ax3 = plt.subplot2grid((9,9), (3,6), colspan=3,rowspan=3)
money_txt = ax3.text(0, 0.8, "money_slope:%s,money_slope_2:%s"%(money_all_half_slope[0],money_all_half_slope[1]), fontsize=15,color='purple')
price_txt = ax3.text(0, 0.6, "price_slope:%s,price_slope_2:%s"%(price_all_half_slope[0],price_all_half_slope[1]), fontsize=15,color='red')
dif1  = round(money_all_half_slope[0] - price_all_half_slope[0],2)
dif2  = round(money_all_half_slope[1] - price_all_half_slope[1],2)
dif_txt = ax3.text(0, 0.4, "all_dif:%s,half_dif:%s"%(dif1,dif2), fontsize=15,color='green')
axcolor = 'lightgoldenrodyellow'
#添加一个轴left, bottom, width, height
data_wave = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)

data_stock = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
data_day = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

#股票信息
def update(val):
    day = int(slider_day.val)
    stock = int(slider_stock.val)
    wave = int(slider_wave.val)
    #根据wave,stock,day获取股票信息
    func_stock_info(wave,stock,day)
def func_stock_info(wn,sn,dayn):
    price, money, x, sname, sid, pzdf_max, pzdf_min, money_max, money_min, next_pzdf_min, next_pzdf_max, next_price, money_all_half_slope, price_all_half_slope = stock_info(wn,sn,dayn)
    title_str = "%s(%s)最高涨幅%s，最低涨幅%s,最大入单%s，最大出单%s" % (sname, sid, pzdf_max, pzdf_min, money_max, money_min)
    ax1.set_title(title_str, fontsize=13)
    ax2.set_title("第二天k线,最高涨幅%s 最低涨幅%s" % (next_pzdf_max, next_pzdf_min))
    line_price.set_ydata(price)
    line_price.set_xdata(x)
    line_money.set_ydata(money)
    line_money.set_xdata(x)
    #更新文本
    money_txt.set_text("money_slope:%s,money_slope_2:%s"%(money_all_half_slope[0],money_all_half_slope[1]))
    price_txt.set_text("price_slope:%s,price_slope_2:%s"%(price_all_half_slope[0],price_all_half_slope[1]))
    dif1 = round(money_all_half_slope[0] - price_all_half_slope[0],2)
    dif2 = round(money_all_half_slope[1] - price_all_half_slope[1],2)
    dif_txt.set_text("all_dif:%s,half_dif:%s" % (dif1, dif2))
    if len(next_price)>0:
        line_price_next.set_ydata(next_price)
        line_price_next.set_xdata(x)

slider_wave = Slider(data_wave, '第几波', 0, 12, valinit=1, valstep=1)
slider_stock = Slider(data_stock, '股票', 0, 10, valinit=1, valstep=1)
slider_day = Slider(data_day, '第几天', 0, 5, valinit=1, valstep=1)
#绑定事件
slider_wave.on_changed(update)
slider_stock.on_changed(update)
slider_day.on_changed(update)
plt.show()