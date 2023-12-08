print("welcome to tresure hunt game \n find the tresure to win the game\n")
task1=input("you are at cross road. where do you to go left or right:")
if task1 == "left":
    task2=input("you have come to lake. do you want to swim or wait:")
    if task2 == "wait":
        task3=input("you have arrived at the bridge. do you want to cross or wait:")
        if task3 == "wait":
            task4=input("you have arrived at a door. do you want to go in door red or blue :")
            if task4 == "red":
                print("you have won the game")
            else:
                print("you have lost the game")
        else:
            print("you have lost the game")
    else:
        print("you have lost the game")
else:
    print("you have lost the game")        
