import csv

def creatfile(name):
    open(name,'x')
    print("File Created! :",name)

def addfriend(name):
    with open(name,'a') as file:
        cfile = csv.writer(file)

        fname = input("Friend's name :")
        pno = input("Phone number :")
        email = input("EMail id :")
        adrs = input("Address :")

        row = [fname,pno,email,adrs]

        cfile.writerow(row)
        print("Friend Added!")
        
def searchfriend(name):

    with open(name,'r') as file:
        cfile = csv.DictReader(file)
        fname = input("Enter Name of your Friend to search :")
        count= 0
        for row in cfile:
            d = dict(row)
            if (fname== d.get("Name")):
                count +=1
                print('A Friend Found :\n Details -> ', d,"\n---------------------")

        print("Total Matches :",count)            



def menu():
    print("1.Create File \n2.Add Friend\n3.Search Friend\n4.Quit")
    inp = int(input("Choose(1,2,3,4):"))
    
    if (inp==1):
        name = input("Enter name of file :")
        creatfile(name)
    elif (inp==2):
        name = input("Enter name of file :")
        addfriend(name)
    elif(inp==3):
        name = input("Enter name of file :")
        searchfriend(name)
    elif(inp==4):
        quit()        

    

    

menu()



