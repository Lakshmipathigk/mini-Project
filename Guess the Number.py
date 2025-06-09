import random
target = random.randint(1,100)

while True:
    userchoice=input("Guess the target: or Quit(Q)")
    if(userchoice== "Q"):
        break
    userchoice=int(userchoice)
    if (userchoice==target):
        print("Sucess: correct Guess !!")
        break
    elif (userchoice > target):
        print("your number is too big. Take smaller guess....")
    else:
        print("your number is too small. Take Biger guess....")
print("----Game Over----")