#encoding=utf8
from mysql import MysqlHelper

# sql='select * from student'
#
# helper = MysqlHelper.MysqlHelper('localhost',3306,'test','root','root')
# one = helper.get_all(sql)
# print(one)
# print(one)
# sid = '121'
# gn_name = 'll'
# zdf = 1
# ctime = 1
# sql = 'insert into tan_plate values(null,%(sid)s,%(gn_name)s,%(zdf)s,%(ctime)s'
# sql='select * from student'
# print(sql)
# params = {"sid": sid, "gn_name": gn_name, "zdf": zdf, 'ctime': ctime}
# helper = MysqlHelper.MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
# print(params)
sid = 'aa'
gn_name = 'bb'
zdf = 1
ctime = 2
#
sql = 'insert into tan_plate values(null,%(sid)s,%(gn_name)s,%(zdf)s,%(ctime)s)'
# sql = "insert into tan_plate values(null,'aa','bb',3,4)"
params = {"sid":sid,"gn_name":gn_name,"ctime":ctime,"zdf":zdf}
helper = MysqlHelper.MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
helper.insert(sql,params)
