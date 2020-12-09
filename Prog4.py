n = int(input("Enter number of people :"))
fare = 0
l18 = 0
l5_17 = 0
for i in range (0,n):
    age = int(input("Enter age for passenger : "+str(i+1)+" : "))
    if(age>=18):
        l18+=1
        fare+=50
    elif(age>=5 and age<18):
        l5_17+=1
        fare+=20
    else:
        continue

print("Age 18 or more :",l18)
print("Age less than 18 and greater than 5:", l5_17)
print("Total fare collected :",fare)        
