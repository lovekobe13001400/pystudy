import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#函数返回一个figure图像和一个子图ax的array列表。
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

#添加一个轴
axindex = plt.axes([0.25, 0.1, 0.65, 0.03])

plt.show()
exit()
#left, bottom, width, height
sindex = Slider(axindex, 'Index', 1, 10, valinit=2, valstep=1)

def update(val):
    index = int(sindex.val)
    ax.clear()
    ax.set_xlabel('index={}'.format(index))
    x = np.arange(0, 2*np.pi, 0.01)
    y = np.sin(x * (2 ** index))
    ax.plot(x, y)
    fig.canvas.draw_idle()
sindex.on_changed(update)
sindex2 = Slider(axindex, 'Index', 5, 20, valinit=2, valstep=2)
update(None)
plt.show()