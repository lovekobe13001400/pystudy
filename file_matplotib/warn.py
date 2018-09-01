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

#第一块
ax1 = plt.subplot2grid((8,9), (0,0), colspan=6,rowspan=6)
ax1.set_title('海康威视（002415）-- 2018-03-02')
#第二块
ax2 = plt.subplot2grid((8,9), (0,6), colspan=3,rowspan=6)
money_txt = ax2.text(0.1, 0.8, "money_slope:%s,money_slope_2:%s", fontsize=15,color='purple')
price_txt = ax2.text(0.1, 0.6, "money_slope:%s,money_slope_2:%s", fontsize=15,color='purple')
dif_txt   = ax2.text(0.1, 0.4, "dif_slope:%s,dif_slope_2:%s", fontsize=15,color='purple')
#三块
axcolor = 'lightgoldenrodyellow'
# ax3 = plt.subplot2grid((8,9), (6,0), colspan=9,rowspan=1)
#添加一个轴left, bottom, width, height
ax_record = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
slider_record = Slider(ax_record, '第几波', 0, 12, valinit=1, valstep=1)
#第四块
ax_day = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
slider_day = Slider(ax_day, '日期', 0, 12, valinit=1, valstep=1)
plt.show()