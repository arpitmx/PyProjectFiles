def getFacto(n):
    if(n==1):
        return n
    elif (n<1):
        return ("Invalid")
    else:
        return n*getFacto(n-1)


s= 0 
x = int(input("input x : "))
n = int(input('input n :'))

for i in range(1,n):
    s += (x**i)/getFacto(i+1)
print("ANS :",s+1)    