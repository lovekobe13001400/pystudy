import redis
res = redis.StrictRedis(host='localhost',port=6379,password='',db=1)
li = {}
li['ip'] = '192.2.4.5'
li['sucess_num'] = 3
li['last_time'] = 111122

res.zadd(li)
print(res)