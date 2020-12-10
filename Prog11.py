
def PUSH(l):
    ll = savelist.l
    ll.append(l)
    savelist(ll)
    return ll


def POP():
    ll = savelist.l
    if not(l.__len__() == 0):
        ll.pop()
        savelist(ll)
        return ll
    else:
        print("Can't Pop, No Items in the list.")
        
    

def PEEK(n):
    ll = savelist.l
    return print("Value at ",n," : ",ll[n])

def TRAVESE():
    ll = savelist.l
    return ll

    
    
    
def savelist(ll):
    savelist.l = ll    



l = []
savelist(l)   

while(True):
    print("===============================\nLIST =>\n",savelist.l,"\n=============================")
    print("1.PUSH\n2.POP\n3.PEEK\n4.TRAVERSE\n5.QUIT")
    inp = int(input("Choose(1,2,3,4) :"))
    if(inp == 1):
        bid = input("Enter id :")
        bn = input("Enter name :")
        ba = input("Enter author :")
        bp = input("Enter publisher :")
        bprice = input("Enter price :")
        l = [bid,bn,ba,bp,bprice]
        lpushed = PUSH(l)
        

    if (inp==2):
        lpop = POP()
        print(lpop)

    if (inp ==3):
        n = int(input("Enter index :"))
        PEEK(n)

    if (inp==4):
        print(TRAVESE())    

    if (inp==5):
        quit()

            


