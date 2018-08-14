#encoding=utf8
import MySQLdb

class MysqlHelper():
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.conn = MySQLdb.connect(host=host, port=port, db=db, user=user, passwd=passwd,charset=charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self,sql,params=()):
        return self.__edit(sql,params)

    def get_one(self,sql,params=()):
        result=None
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
        except Exception as e:
            print(e.message)
        return result

    def get_all(self,sql,params=()):
        list=()
        try:
            self.cursor.execute(sql,params)
            list=self.cursor.fetchall()
        except Exception as e:
            print(e.message)
        return list



    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self,sql,params):
        count=0
        try:
            count=self.cursor.execute(sql,params)
            self.conn.commit()
        except Exception as e:
            print(e.message)
        return count
# helper = MysqlHelper('localhost', 3306, 'mystock', 'root', 'root')
# params = {'name': '阿里巴巴概念', 'sid': 'aa', 'price': 1109.905, 'time_point': 930.0, 'date': '2018-06-14', 'zdf': -0.54, 'pre': 1115.926, 'volume': 5475532}
# print(params)
# sql = 'insert into tan_plate_record values(null,%(name)s,%(sid)s,%(price)s,%(time_point)s,%(date)s,%(zdf)s,%(pre)s,%(volume)s)'
# helper.insert(sql,params)

