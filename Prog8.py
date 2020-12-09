print("==========================>\n\n1.Create File \n2.Search occurrences of a word \n3.Search occurrences of a letter \n4.Quit")
inp= int(input("Enter your Choice :"))

if (inp ==1):
    name = input("Enter file name :")
    file = open(name ,'x')
    print("File Created.")
    file.close()

if (inp ==2):
    name = input('Enter file name :')
    file= open(name,"r")
    inp = input("Input the word to count the occurrences : ")
    count = 0
    
    for line in file:
        line.replace('\n',"")
        l = line.split(" ")
        for i in l:
            if(i==inp):
                count+=1
        
            
    print("Total occurence of "+inp+" :",count)            
             
if (inp ==3):
    name = input('Enter file name :')
    file= open(name,"r")
    inp = input("Input the letter to count the occurrences : ")
    count = 0
    
    for line in file:
        for letter in line:
            if(letter == inp):
                count+=1
if (inp ==4):
    print("Closing application...")
    

        
            
             
    
