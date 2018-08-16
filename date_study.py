from datetime import datetime
from datetime import timedelta
#1.datetime.now()返回当前日期和时间，其类型是datetime。
now = datetime.now()

#2.转时间戳
now_stamp = now.timestamp()

#3timestamp转换为datetime
now_date = datetime.fromtimestamp(now_stamp)


#4.str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

#5.datetime转换为str
day_str = now.strftime('%Y-%m-%d %H:%M:%S')

#6.datetime加减
new_day = now - timedelta(days=1)
print(new_day)