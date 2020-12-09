a = (1,2,42,0,3,-1,4,5,24)
max = a[0]
min = a[0]

for i in a:
    if max<i:
        max = i
    elif min>i:
        min = i
        
print("max :",max)
print("min :",min)            
    
