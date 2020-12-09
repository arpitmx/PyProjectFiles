print("==========================>\n\n1.Create File \n2.Add appilicant \n3.Search Applicant on the basis of qualification\n4.Modify Appilcant \n5.Quit")

inp= int(input("Enter your Choice :"))

if (inp ==1):
    name = input("Enter file name :")
    file = open(name ,'x')
    print("File Created.")
    file.close()

if (inp ==2):
    name = input('Enter file name :')
    file= open('data.dat',"a")
    aId = input("Enter application id : ")
    aName = input("Enter application name : ")
    aQual = input("Enter Qualification : ")

    file.writelines("\n"+aId+","+aName+","+aQual)
    file.close()
             
if (inp ==3): 
    name = input('Enter file name :')
    file= open(name,"r")
    inp = input("Input Qualification :")
    l = []
    lfinal = []
    for line in file:
    
        line = line.rstrip()
        l=line.split(",")
    
        if(l[2]==inp):
            lfinal.append(l[1])
    print("Applicants with matching Qualifications :",lfinal)        

        


if (inp ==4):
    name = input('Enter file name :')
    fileOld= open(name,"r")
    fileUpdated= open("updated"+name,"w")
    inp = input("Input Application id to modify details :")
    aName = input("Enter new application name  : ")
    aQual = input("Enter new Qualification : ")
    
   
    for line in fileOld.readlines():

        if not(line.startswith(inp)):
            fileUpdated.write(line)
    fileUpdated.write("\n"+inp+","+aName+","+aQual)
    fileOld.close()
    fileUpdated.close() 

if(inp==5):
    print(">Quit")    



        

    
    

        
            
             
    
