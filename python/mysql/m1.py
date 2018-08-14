import MySQLdb
conn=MySQLdb.connect(host='localhost',port=3306,db='test',user='root',passwd='root',charset='utf8')
cs1=conn.cursor()
count=cs1.execute("insert into student(name) values('张良')")
print(count)
conn.commit()
cs1.close()
conn.close()