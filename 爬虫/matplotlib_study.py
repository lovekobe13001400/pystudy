#折线图
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
x = np.arange(9)
y = np.sin(x)
z = np.cos(x)
xList = []
yList = []
for i in range(1000):
    xList.append(i)
    yList.append(i)

# #marker数据点样式，linewidth线宽，linestyle线型样式，color颜色
# plt.plot(x,y,marker='.',linewidth=3,linestyle='--',color='orange')
# plt.plot(x,z)
# plt.plot(xList,yList)
# plt.title('XX图')
# plt.xlabel('height')
# plt.ylabel('width')
# #设置图例
# plt.legend(['Y','Z'],loc='upper right')
# plt.grid(True)
# plt.show()

#散点图
# x = np.random.rand(10)
# y = np.random.rand(10)
# plt.scatter(x,y)
# plt.show()
#柱状图
# x = np.arange(10)
# y = np.random.randint(0,30,10)
# plt.bar(x,y)
# plt.show()

#饼图
# x = np.random.randint(1,10,3)
# plt.pie(x)
# plt.show()

#z直方图(疑问)
# mean, sigma = 0, 1
# x = 0 + sigma * np.random.randn(100)
# print(x)
# plt.hist(x,10)
# plt.show()

# figsize绘图对象的宽度和高度，单位为英寸，dpi绘图对象的分辨率，即每英寸多少个像素，缺省值为80
# plt.figure(figsize=(8,6),dpi=100)
# A = plt.subplot(2,2,1)
# plt.plot([0,1],[0,1], color="red")
#
#
# plt.subplot(2,2,2)
# plt.title("B")
# plt.plot([0,1],[0,1], color="green")
#
#
# plt.subplot(2,1,2)
# plt.title("C")
# plt.plot(np.arange(10), np.random.rand(10), color="orange")
#
#
#
# plt.show()

x = np.arange(30)
y = np.sin(x)
plt.figure(figsize=(12,6))
plt.gca().xaxis.set_major_locator(MultipleLocator(3))
plt.gca().xaxis.set_major_formatter(FormatStrFormatter("%d-K"))
# 自动旋转X轴的刻度，适应坐标轴
#plt.gcf().autofmt_xdate()
plt.plot(x,y)
plt.show()