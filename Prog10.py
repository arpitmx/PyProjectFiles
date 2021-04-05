import csv
def create():
    f=open('myCSV.csv','w')
    print()
    print('File Created')
    print()
    f.close()

def add():
    f=open('myCSV.csv','a')
    
    name=input("Enter Name: ")
    no=int(input("Enter Mobile No.: "))
    email=input("Enter Email: ")
    add=input("Enter Address: ")
    print()
    print("Done")
    print()
    friend=[name,no,email,add]
    fwriter = csv.writer(f)
    fwriter.writerow(friend)
    f.close()

def search():
    friend=input("Enter Name: ")
    f=open("myCSV.csv",'r')
    freader=csv.reader(f)
    for i in freader:
        if i[0]==friend:
            print('Found!')
            print(i) 
            break
    
        
    f.close()

while True:
    ch=int(input("Enter choice: 1. Create File\n 2. Add Friend\n 3. Search Friend\n 4.Quit\n"))
    if ch==1:
        create()
    elif ch==2:
        add()
    elif ch==3:
        search()
    else:
        break
