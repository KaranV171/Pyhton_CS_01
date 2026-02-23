import random
print("Game Start")
com = random.randint(0,100)

while(1):
    print("Enter your guess ")
    us = int(input())
    if(us<com):
        print("Number is lesser than guess number")
    elif(us>com):
        print("Number is greater than guess number")
    else:
        print("You Win")
        break

print("Game End")