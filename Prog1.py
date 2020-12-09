
def doMath(inp, n1,n2):
    print("Choosed :"+inp)

    switcher = {
        '1': n1+n2,
        '2': n1-n2,
        '3': n1/n2,
        '4': n1*n2
    }

    return print("Ans :",switcher.get(inp,"error value "),"\n============================")

while (True):
    print("====================================\n")    
    print("1.add \n2.sub \n3.div \n4.mul \n5.Quit")
    inp = input("\n>Enter choice :")
    n1= int(input("Enter Num 1:"))
    n2= int(input("Enter Num 2:"))
   
    l1 = ['1','2','3','4']
    l2 = ['add','sub','div','mul']
    lf = l1+l2
    
    if (inp in l1):
        doMath(inp, n1,n2)

    elif (inp in l2):
        doMath(l1(inp-1),n1,n2)


    else:
        print("Closing application")    
    
    




