import pymysql.cursors
connector = pymysql.connect(host='localhost',user='root',password='')
cursor = connector.cursor()

#cursor.execute("create database students ")
cursor.execute("use students")
cursor.execute("""CREATE TABLE STest1 (
                    Nos int NOT NULL AUTO_INCREMENT,
                    Name varchar(100) NOT NULL,
                    Stipend int NOT NULL,
                    Stream varchar(100) NOT NULL,
                    AvgMark float(3,1) NOT NULL,
                    Grade char(1) NOT NULL,
                    Class varchar(4) NOT NULL,
                    PRIMARY KEY(Nos)
                    );""")

#inputs :
name = input("Name:")
sti = input("Stipend :")
stream = input("Stream:")
avg = input("avg:")
grade = input("grd:")
clss = input("class:")

cursor.execute("INSERT INTO STest1 (Name,Stipend,Stream,AvgMark,Grade,Class) VALUES(%s,%s,%s,%s,%s,%s)",
               (name,sti,stream,avg,grade,clss))
connector.commit()

print("1 ROW INSERTED....")

