import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from mysql.MysqlHelper import *
from pylab import mpl

fig = plt.figure()
fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

text2 = ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, u'unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)


ax.plot([2], [1], 'o')
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.axis([0, 10, 0, 10])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sfreq = Slider(axfreq, '周几', 0, 5, valinit=1, valstep=1)
def update(val):
    # amp = samp.val
    freq = sfreq.val
    text2.set_text('dd')
    fig.canvas.draw_idle()


sfreq.on_changed(update)
plt.show()