#python访问数据库

#数据库服务运行ip地址、端口、数据库用户名/密码

import MySQLdb
conn = MySQLdb.connect(
    host="192.168.1.104",
    port="330",
    user="songqin",
    passwd="songqin",
    db="plesson",  #数据库名
    charset="utf8"
)

c = conn.cursor()  #游标对象cursor，发送sql语句
c.execute("select * from sq_course")
c.execute("INSERT INTO sq_course(NAME,`desc`,display_idx) VALUES('mts','python———no.2',13)")
#列名desc与倒序排列desc关键字一样，最好用反斜杠括起来
conn.commit()  #插入操作需要coomit一下
conn.close()

#rows = c.fetchall()
#print(rows)

for i in range(c.rowcount): #游标对象的属性rowcount，可以知道有多少条记录
    row = c.fetchone()
    #rows = c.fetchmany(100)
    if row[1] == "Python":
        print("检查点===> Python课程找到，通过")
        break



