import random

pscr1 =0 
pscr2 =0


while(True):
    input("=====================\nPlayer1 Chance : Press Enter")
    n1 = random.randrange(1,6)
    pscr1 += n1 
    print("Dice :",n1)
    print("Player1 Score :",pscr1)

    input("\nPlayer2 Chance : Press Enter")
    n2 = random.randrange(1,6)
    pscr2 += n2 
    print("Dice :",n2)
    print("Player2 Score :",pscr2,"\n==========================>")

    if(pscr1 >=20 ):
        print("\n=======>Player1 WON!<=======")
        break

    elif(pscr2 >=20 ):
        print("=======>Player2 WON!<=======")
        break    

    elif(pscr1>=20 and pscr2>=20):
        print("DRAW!")
        break    