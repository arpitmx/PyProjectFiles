import pymysql.cursors

connector = pymysql.connect(host = 'localhost',user='root',password='')

cursor = connector.cursor()

#cursor.execute("create database club1")
cursor.execute("use club1")
sql = """create table ctable2 (COACHID int AUTO_INCREMENT NOT NULL,
COACHNAME varchar(100) NOT NULL, AGE int NOT NULL, SPORTS varchar(100) NOT NULL ,
DATEOFAPP DATE NOT NULL , PAY int NOT NULL, SEX char(1), PRIMARY KEY(COACHID));"""

#cursor.execute(sql)
cursor.execute("INSERT INTO ctable2 (COACHNAME,AGE,SPORTS,DATEOFAPP,PAY,SEX) VALUE('test1',20,'Football','2001-03-02',4000,'M');")
connector.commit()
cursor.execute("INSERT INTO ctable2 (COACHNAME,AGE,SPORTS,DATEOFAPP,PAY,SEX) VALUE('test2',40,'Baseball','2001-03-02',4000,'M');")
connector.commit()
cursor.execute("SELECT * FROM ctable2")
result = cursor.fetchall()
j = 0
for i in result:
    print
    print(result[j],"\n----------------------------------------------")
    j = j+1





