import os
names = os.listdir('../')

print(names)

#过滤

names = [name for name in os.listdir('../') if os.path.isfile(os.path.join('../',name))]

dirnames = [name for name in os.listdir('../') if os.path.isdir(os.path.join('../',name))]


print(dirnames)


#对于文件名的匹配

import glob

pyfiles = glob.glob('../*.txt')
print(pyfiles)
from fnmatch import fnmatch

pyfiles = [name for name in os.listdir('../') if fnmatch(name,'*.txt')]

print(pyfiles)