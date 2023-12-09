import random
print("\n ****Welcome to rock paper scissors game**** ")
user=int(input("Enter 1 for rock 2 for paper and 3 for scissors:"))
bot = random.randint(1,3)
if user == bot :
    print("it's a tie ")
else :
    if user == 1 :
        if bot == 2 :
            print("you lose ")
        else :
            print("you win ")
    elif user == 2 :
        if bot == 3 :
            print("you lose ")
        else :
            print("you win ")
    elif user == 3 :
        if bot == 1 :
            print("you lose ")
        else :
            print("you win ")
    else :
        print("invalid input ")    
    