#add friends , modify friends details , search friends details : details => name , pno.
import pymysql.cursors
connector = pymysql.connect(host='localhost',user='root',password='')
cursor = connector.cursor()

#friends table  desc >  name (varchar) , password(varchar)
#cursor.execute("create database fdb")
cursor.execute("use fdb")
#sql_command = """CREATE TABLE friends (name VARCHAR(30),pno VARCHAR(10) );"""
#cursor.execute(sql_command)


def addf(name,pno):
    sql = "INSERT INTO `friends` (`name`,`pno`) VALUES (%s,%s)"
    cursor.execute(sql,(name,pno))
    connector.commit()

def modifyf():
    pno = input("Enter Pno. of your friend :")
    sql = "SELECT `name` FROM `friends` WHERE `pno`=%s"
    cursor.execute(sql,pno)
    result = cursor.fetchone()
    print("Name :",result[0])
    if result[0] is None:
        print("Friend not found!")
    else:
        inp = int(input("Input what to change : \n1.Name \n2.Phone Number"))
        if (inp==1):
            name= input("Enter the new name :")
            sql = "UPDATE friends SET name = %s WHERE pno = %s;"
            value = (name,pno)
            cursor.execute(sql,value)
            connector.commit()
        if (inp==2):
            pno = input("Enther the new Phone Number :")
            sql = "UPDATE friends SET pno = %s WHERE name = %s;"
            value = (pno,result[0])
            cursor.execute(sql,value)    
            connector.commit()
            
def searchf(name):
    sql = "SELECT pno FROM friends WHERE name=%s;"
    value = (name)
    cursor.execute(sql,value)
    connector.commit()
    result = cursor.fetchone()
    if (result != None):
        print("Name :"+name+" Phone no. :",result[0])
    else:
        print("Friend Not Found")

while(True):
    inp = int(input("\n 1:Add Friend \n 2:Modify Details \n 3:Search Details \n 4:Quit \n >"))
    if(inp==1):
        name = input("Name:")
        phone = input("Pno.:")
        addf(name,phone)
    elif(inp==2):
        modifyf()
    elif(inp==3):
        name = input("Name:")
        searchf(name)

    elif(inp==4):
        quit()
        
        
    
    
    
            
        
