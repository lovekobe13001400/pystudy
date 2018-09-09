a = {'x':1,'z':3}
b = {'y':2,'z':4}

from collections import ChainMap
c = ChainMap(a,b)
#现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）。
# 一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。比如：
print(c['x'])
print(c['y'])
print(c['z'])

#方法2
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

merged = dict(b)
merged.update(a)#有更新，没有添加
print(merged)


