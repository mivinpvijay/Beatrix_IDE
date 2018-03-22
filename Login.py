import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='beatrix')
a=conn.cursor()
sql='SELECT * from users;'
a.execute(sql)
countrow=a.execute(sql)
print("Number of rows:",countrow)
data=a.fetchone()
print(data)
