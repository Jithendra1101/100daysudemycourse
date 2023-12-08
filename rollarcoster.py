print("welcome to rollar coster ride :")
height = int(input("enter your height in cm :"))
bill = 0
if height >= 120:
    print("you can ride the rollar coster ride")
    age = int(input("enter your age :"))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print("adult tickets are $12")
    photo = input("do you want to take photo ? Y or N :")
    if photo == "Y":
        bill += 3
    print(f"your final bill is {bill}")
    print("thank you for riding rollar coster ride")
else :
    print ("you can't ride the rollar coster ride")    