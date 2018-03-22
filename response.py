import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='questions')
a=conn.cursor()
def getrespo(code):
    sql='SELECT * from que where code=%d'%code
    a.execute(sql)
    countrow=a.execute(sql)
    print("Number of rows:",countrow)
    data=a.fetchone()
    return data[1]

getrespo(3)
