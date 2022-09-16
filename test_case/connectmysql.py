import pymysql

# db=pymysql.Connect('114.55.43.36','haibao','haibao1234','test')
# cursor=db.cursor()
# cursor.execute('select * from websites')
# data=cursor.fetchone()
# print(data)

db=pymysql.connect('114.55.43.36','haibao','haibao1234','test')
cursor=db.cursor()
#
sql='''create table rmployee(
#         first_name  char(20) not null,
#         last_name   char(20),
#         age tinyint(4),
#         sex char(1),
#         income float)'''
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()


# sql='''insert into rmployee(first_name,
# last_name,age,sex,income)
# values('mac','Mohan',20,'M',2000)'''
# cursor.execute(sql)
# db.commit()
# db.close()

# sql='''select * from rmployee where income>1000'''
# cursor.execute(sql)
# data=cursor.fetchone()
# print(data)

# sql='''update rmployee set age=age+1 where sex='M'
# '''
# cursor.execute(sql)
# db.commit()
# db.close()

sql='''select * from rmployee'''
cursor.execute(sql)
data=cursor.fetchall()
print(data)




