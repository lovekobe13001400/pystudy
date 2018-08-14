import pymysql.cursors

# 连接数据库

class MysqlHelper():
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost', port=3306, db='mystock', user='root', passwd='root',charset='utf8')
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
# 获取游标
