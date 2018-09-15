from datetime import timedelta

#时间段
a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)

c = a + b #datetime.timedelta(2, 37800)
c
c.days #2
c.seconds#37800
c.total_seconds()#总描述

from datetime import datetime
a = datetime(2012,9,23,1,1)
b = datetime(2012,12,21)
b-a #datetime.timedelta(88, 82740)

#
datetime.now()   #datetime.datetime(2018, 9, 10, 13, 47, 33, 37110)
datetime.today() #datetime.datetime(2018, 9, 10, 13, 47, 43, 270133)


#对大多数基本的日期和时间处理问题， datetime 模块已经足够了。 如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块



#计算最后的周五
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname,start_date=None):
    if start_date is None:
        start_date = datetime.today()
    #一周的第几天，0是星期一
    day_num = start_date.weekday()
    #目标星期是第几个比如星期一就是0，
    day_num_target = weekdays.index(dayname)

    days_ago = (7 + day_num - day_num_target)%7

    if days_ago == 0:
        days_ago = 7
    #差多少个时间段
    target_date = start_date - timedelta(days=days_ago)
    return target_date

#上一个星期一
get_previous_byday('Monday')


##
from datetime import datetime, date, timedelta
import calendar

def get_monty_range(start_date = None):
    if start_date is None:
        #当前月份的第一天
        start_date = date.today().replace(day = 1)

    #XX年 XX月总共有多少天
    _,days_in_month = calendar.monthrange(start_date.year,start_date.month)
    #days_in_month 这个月有几天
    end_date = start_date + timedelta(days = days_in_month)
    return (start_date,end_date)

a_day = timedelta(days = 1)
#主要就是获取起始时间和结束时间
first_day,last_day = get_monty_range()

#在这样的日期上循环并需要事先构造一个包含所有日期的列表
while first_day<last_day:
    print(first_day)
    first_day += a_day


#
def date_range(start,stop,step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2012,9,1),datetime(2012,9,3),timedelta(hours=6)):
    print(d)


#
y = datetime.strptime('2012-09-20','%Y-%m-%d')
