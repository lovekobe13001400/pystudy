import os

path = './Users/bea/DAta/a.txt'

#文件名
print(os.path.basename(path))

#目录

print(os.path.dirname(path))


#组建目录

print(os.path.join('tmp','book','a.txt'))

#
path = '~/Data/data.csv'

os.path.expanduser(path)

#he user's home directory
print(os.path.expanduser(path))

#
print(os.path.split(path))