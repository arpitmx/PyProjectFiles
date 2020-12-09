def checklast(n):
    if(n%10==5):
        return 1
    else:
        return 0

l = [102,105,11,15,235,3425,4,5]        
l2 = []
for i in l:
    l2.append(checklast(i))

print(l2)    