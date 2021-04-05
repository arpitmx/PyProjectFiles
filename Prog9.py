import pickle
print("==========================>\n\n1.Create File \n2.Add appilicant \n3.Search Applicant on the basis of qualification\n4.Modify Appilcant \n5.Quit")

inp= int(input("Enter your Choice :"))

if (inp ==1):
    file = open('data.DAT' ,'wb')
    print("File Created.")
    file.close()

if (inp ==2):
   
    file= open('data.DAT',"ab")
    aId = input("Enter application id : ")
    aName = input("Enter application name : ")
    aQual = input("Enter Qualification : ")
    
    l = [aId,aName,aQual]
    pickle.dump(l,file)
    file.close()
             
if (inp ==3): 
    
    file= open('data.DAT',"r")
    inp = input("Input Qualification :")
    lfinal = []
    try:
        while True:
            appln=pickle.load(f)
            if appln[2]==inp:
                print(appln)
                lfinal.append(appln)
        print("Applicants with matching Qualifications :",lfinal)              
    except EOFError :
        f.close()
         

        


if (inp ==4):
    
    app=[]
	f=open('APPLICANT.DAT','rb+')
	id=int(input('Enter id to search  '))
	qual=input('Enter new qualification  ')
	try:
		while True:
			rp=f.tell()
			app=pickle.load(f)
			if app[0]==id:
				app[2]=qual
				f.seek(rp)
				pickle.dump(app,f)
				break
	except EOFError:
		f.close()

if(inp==5):
    print(">Quit")    



        

    
    

        
            
             
    
