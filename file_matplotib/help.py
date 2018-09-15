#coding=utf-8
import numpy as np
import json
from datetime import timedelta,date
import datetime
from mysql.MysqlHelper import *
#返回斜率
def fitSLR(x,y):
    n=len(x)    #获取x的长度，x是list
    if n<=1:
        return 0
    dinominator = 0.0#初始化分母
    numerator=0.0     #初始化分子
    for i in range(0,n):    #求b1

        numerator += (x[i]-np.mean(x))*(y[i]-np.mean(y))

        dinominator += (x[i]-np.mean(x))**2 #**表示平方


    b1 = numerator/float(dinominator)   #得出b1,斜率
    b0 = np.mean(y)/float(np.mean(x))   #得出b0
    #y = b0+x*b1
    return b1
    #return b0,b1
def realPoint(min,max,val):
    #200个点代表max - min
    return -100+(val -min)/(max - min)*200

#获取第几波 第几只股票 第几天的price和money处理好的斜率
def stock_info(wn,sn,dayn):
    #now = datetime.datetime.now() - timedelta(days=4)
    now = datetime.datetime.now()
    this_week_start = now - timedelta(days=now.weekday())
    day1 = this_week_start.strftime('%Y-%m-%d')
    day2 = (this_week_start + timedelta(days=1)).strftime('%Y-%m-%d')
    day3 = (this_week_start + timedelta(days=2)).strftime('%Y-%m-%d')
    day4 = (this_week_start + timedelta(days=3)).strftime('%Y-%m-%d')
    day5 = (this_week_start + timedelta(days=4)).strftime('%Y-%m-%d')
    weekday_arr = [0, day1, day2, day3, day4, day5]
    db = MysqlHelper()
    all_stock_sql = "select * from tan_stock where is_big=2"
    all_stock = db.get_all(all_stock_sql)
    stockn = int((wn - 1) * 10 + sn)
    sid = all_stock[stockn - 1][1]
    sname = all_stock[stockn - 1][2]
    sql = "select * from tan_stock_record where sid='%s' and date='%s'" % (sid, weekday_arr[dayn])

    stock_info = db.get_all(sql)
    if len(stock_info)==0:
        #return price, money, x, sname, sid, pzdf_max, pzdf_min, money_max, money_min, next_pzdf_min, next_pzdf_max, next_price
        return [], [], [], sname, sid, 0, 0, 0, 0, 0, 0, [],(0,0),(0,0)
    price = []
    money = []
    x = []
    xi = 0
    price_min = 9999999
    price_max = -9999999
    money_min = 9999999
    money_max = -99999999
    price_all_half_slope = (0,0)
    money_all_half_slope = (0,0)
    # 只为了得出最大值和最小值
    pre = 0
    for one_stock in stock_info:
        # 占多少格
        pre = one_stock[7]
        temp_price = one_stock[3]
        temp_money = (one_stock[9] - one_stock[10] + one_stock[11] - one_stock[12])/10000
        if temp_price > price_max:
            price_max = temp_price
        if temp_price < price_min:
            price_min = temp_price
        if temp_money > money_max:
            money_max = temp_money
        if temp_money < money_min:
            money_min = temp_money


    pzdf_min = round((price_min-pre)/pre*100,1)
    pzdf_max = round((price_max-pre)/pre*100,1)



    #计算斜率
    for one_stock in stock_info:
        xi += 1
        x.append(xi)
        # 占多少格
        temp_price = one_stock[3]
        temp_money = (one_stock[9] - one_stock[10] + one_stock[11] - one_stock[12]) / 10000
        price.append(realPoint(price_min, price_max, temp_price))
        money.append(realPoint(money_min, money_max, temp_money))

    #获取第二天股价的最高涨幅和最低涨幅
    if dayn == 5:
        next_pzdf_min, next_pzdf_max = 0,0

        next_price = []
    else:
        sql = "select * from tan_stock_record where sid='%s' and date='%s'" % (sid, weekday_arr[dayn+1])
        stock_info = db.get_all(sql)

        price_max = -9999999
        price_min = 9999999
        # 只为了得出最大值和最小值
        pre = 0
        for one_stock in stock_info:
            # 占多少格
            pre = one_stock[7]
            temp_price = one_stock[3]
            if temp_price > price_max:
                price_max = temp_price
            if temp_price < price_min:
                price_min = temp_price
        #100等分
        next_price = []
        for one_stock in stock_info:
            # 占多少格
            next_price.append(realPoint(price_min,price_max,one_stock[3]))


        next_pzdf_min = round((price_min - pre) / pre * 100, 1)
        next_pzdf_max = round((price_max - pre) / pre * 100, 1)
        #price,money是计算好的斜率
        money_all_half_slope = all_half_slope(x,money)
        price_all_half_slope = all_half_slope(x,price)

    return price,money,x,sname,sid,pzdf_max,pzdf_min,money_max,money_min,next_pzdf_min,next_pzdf_max,next_price,money_all_half_slope,price_all_half_slope

#全部点和后半段的斜率
def all_half_slope(x,y):
    n = len(x)  # 获取x的长度，x是list
    if n <= 1:
        return 0
    dinominator = 0.0  # 初始化分母
    numerator = 0.0  # 初始化分子

    half_x = []
    half_y = []
    for i in range(0, n):  # 求b1
        numerator += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x)) ** 2  # **表示平方
        if i>=n/2:
            half_x.append(x[i])
            half_y.append(y[i])
    all_slope = numerator / float(dinominator)  # 得出b1,斜率

    half_dinominator = 0.0  # 初始化分母
    half_numerator = 0.0  # 初始化分子
    half_n = len( half_x)
    # print(half_n)
    # print(half_x)
    # print(half_y)
    for j in range(0, half_n):  # 求b1
        half_numerator += (half_x[j] - np.mean(half_x)) * (half_y[j] - np.mean(half_y))
        half_dinominator += (half_x[j] - np.mean(half_x)) ** 2  # **表示平方

    half_slope =  half_numerator / float(half_dinominator)  # 得出b1,斜率
    return round(all_slope,2),round(half_slope,2)


def stock_today(sn=1):
    offset = sn-1
    today  = datetime.datetime.now().strftime('%Y-%m-%d')

    sql = "SELECT * from tan_stock_content WHERE date='%s' order by id desc LIMIT %s,1"%(today,offset)
    # print(sql)
    db = MysqlHelper()
    stock_info = db.get_one(sql)
    price_content = stock_info[2]
    money_content = stock_info[3]
    sid = stock_info[1]

    key = 'hs_%s'%(sid)
    price_dict = decode_stock_json(price_content)
    money_dict = decode_stock_json(money_content)

    price_data = price_dict[key]['data'].split(';')
    is_stop = price_dict[key]['stop']
    #停牌
    if is_stop:
        #price, money, x, sname, sid, pzdf_max, pzdf_min,money_max, money_min, money_all_half_slope, price_all_half_slope
        sql = "select * from tan_stock where sid='%s'" % (sid)

        stock = db.get_one(sql)
        sname = stock[2]
        return [],[],[],'%s停牌'%(sname),sid,0,0,0,0,(0,0),(0,0)
    pre = float(price_dict[key]['pre'])
    money_data = money_dict[key]['data'].split(';')
    #price所有价格集合，所有money集合
    price = []
    money = []
    x = []
    xi = 0

    price_min = 9999999
    price_max = -9999999
    money_min = 9999999
    money_max = -99999999
    price_all_half_slope = (0, 0)
    money_all_half_slope = (0, 0)
    # 只为了得出最大值和最小值

    for i in range(len(price_data)):
        xi += 1
        x.append(xi)
        price_temp_arr = price_data[i].split(',')
        temp_price = float(price_temp_arr[1])
        money_temp_arr = money_data[i].split(',')
        temp_money = ( float(money_temp_arr[1]) - float(money_temp_arr[2]) + float(money_temp_arr[3]) - float(money_temp_arr[4]) ) /1000

        if temp_price > price_max:
            price_max = temp_price
        if temp_price < price_min:
            price_min = temp_price
        if temp_money > money_max:
            money_max = temp_money
        if temp_money < money_min:
            money_min = temp_money

    pzdf_min = round((price_min - pre) / pre * 100, 1)
    pzdf_max = round((price_max - pre) / pre * 100, 1)
    for i in range(len(price_data)):
        #第i个点
        #股价
        price_temp_arr = price_data[i].split(',')
        temp_price = float(price_temp_arr[1])

        #大单
        money_temp_arr = money_data[i].split(',')
        temp_money = ( float(money_temp_arr[1]) - float(money_temp_arr[2]) + float(money_temp_arr[3]) - float(money_temp_arr[4]) ) /1000

        price.append(realPoint(price_min, price_max, temp_price))
        money.append(realPoint(money_min, money_max, temp_money))



    sql = "select * from tan_stock where sid='%s'"%(sid)

    stock = db.get_one(sql)
    sname = stock[2]

    money_all_half_slope = all_half_slope(x, money)
    price_all_half_slope = all_half_slope(x, price)

    return price, money, x, sname, sid, pzdf_max, pzdf_min,money_max, money_min, money_all_half_slope, price_all_half_slope

def decode_stock_json(content):

    c1 = content.split('last(')[1].strip(')')
    c2 = json.loads(c1)
    return c2

if __name__ == '__main__':
    x = [122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242]
    y = [ -67.79661016949191, -59.32203389830594, -52.542372881355725, -52.542372881355725, -35.59322033898381, -27.118644067796637, -40.67796610169586, -40.67796610169586, -50.84745762711877, -50.84745762711877, -57.627118644067785, -67.79661016949191, -66.10169491525495, -66.10169491525495, -67.79661016949191, -50.84745762711877, -28.81355932203479, -33.898305084745644, -37.28813559322076, -52.542372881355725, -57.627118644067785, -50.84745762711877, -54.237288135593886, -57.627118644067785, -64.4067796610168, -57.627118644067785, -59.32203389830594, -67.79661016949191, -84.74576271186503, -100.0, -93.220338983051, -77.96610169491602, -64.4067796610168, -62.711864406779846, -79.66101694915297, -69.49152542372886, -76.27118644067787, -71.18644067796701, -69.49152542372886, -81.35593220338993, -76.27118644067787, -83.05084745762808, -79.66101694915297, -76.27118644067787, -69.49152542372886, -64.4067796610168, -57.627118644067785, -57.627118644067785, -50.84745762711877, -47.45762711864487, -45.76271186440671, -28.81355932203479, -25.42372881355969, -23.72881355932273, -33.898305084745644, -50.84745762711877, -33.898305084745644, -47.45762711864487, -59.32203389830594, -50.84745762711877, -50.84745762711877, -54.237288135593886, -64.4067796610168, -59.32203389830594, -55.93220338983084, -54.237288135593886, -57.627118644067785, -59.32203389830594, -59.32203389830594, -64.4067796610168, -81.35593220338993, -83.05084745762808, -83.05084745762808, -76.27118644067787, -81.35593220338993, -83.05084745762808, -98.30508474576305, -93.220338983051, -84.74576271186503, -54.237288135593886, -61.01694915254289, -66.10169491525495, -62.711864406779846, -69.49152542372886, -71.18644067796701, -55.93220338983084, -38.98305084745771, -28.81355932203479, -42.37288135593281, -35.59322033898381, -27.118644067796637, -40.67796610169586, -37.28813559322076, -38.98305084745771, -50.84745762711877, -64.4067796610168, -66.10169491525495, -50.84745762711877, -42.37288135593281, -45.76271186440671, -45.76271186440671, -37.28813559322076, -44.067796610169765, -54.237288135593886, -42.37288135593281, -38.98305084745771, -52.542372881355725, -54.237288135593886, -61.01694915254289, -66.10169491525495, -62.711864406779846, -64.4067796610168, -67.79661016949191, -72.88135593220396, -69.49152542372886, -71.18644067796701, -74.57627118644092, -74.57627118644092, -71.18644067796701]

    print(stock_today(1))
    exit()
