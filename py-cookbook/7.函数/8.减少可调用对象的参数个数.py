

#partial() 函数来固定某些参数值：

from functools import partial
def spam(a,b,c,d):
    print(a,b,c,d)
s1 = partial(spam,1)
s1(2,3,4)

s2 = partial(spam,d=34)
s2(1,2,3)


#使用1

points = [(1,2),(3,4),(5,6),(7,8)]

import math

def distance(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    #print(p1)
    #hypot() 返回欧几里德范数 sqrt(x*x + y*y)。
    return math.hypot(x2-x1,y2-y1)
#基点
pt = (4,3)


#按照根据基点的距离进行排序

#p1是基点 p2是pt
points.sort(key=partial(distance,pt))
print(points)



#
def output_result(result,log=None):
    if log is not None:
        log.debug('Got:%r',result)


def add(x,y):
    return x+y

import logging
from multiprocessing import Pool
from functools import partial

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test')

p = Pool()
