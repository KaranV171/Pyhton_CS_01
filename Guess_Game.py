import random
print("Game Start")
com = random.randint(0,100)
count=0
while(1):
    print("Enter your guess ")
    us = int(input())
    count=count+1
    if(us<com):
        print("Number is lesser than guess number")
    elif(us>com):
        print("Number is greater than guess number")
    else:
        print("You Win")
        break
print(f"You Guess the number in {count} attempt")
print("Game Over")