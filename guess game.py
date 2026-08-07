import random

target = random.randint(1,100)

while True:
    userchoice = int(input("Guess The Number : "))

    if (userchoice == quit):
        break

    elif (userchoice == target):
        print("/n Genius You are Corrcet")
        break


    elif (userchoice >= target):
         print( " THe NUmber is to bigg") 

    else:
        print(" The number is to small")

print(".......................GAME OVER................")    



            
    
