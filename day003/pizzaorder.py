print("\n welcome to pizza shop \n")
size = input("what size pizza do you want? S,M,L \n")
add_pepperoni = input("do you want pepperoni? Y,N \n")
extra_cheese = input("do you want extra cheese? Y,N \n")
bill = 0
if size == "S":
    bill +=15
    if add_pepperoni == "Y":
        bill +=2
    else:
        bill +=0
    if extra_cheese == "Y":
        bill +=1
    else: 
        bill +=0
elif size == "M":
    bill +=20
    if add_pepperoni == "Y":
        bill +=3
    else:
        bill +=0
    if extra_cheese == "Y":
        bill +=1
    else: 
        bill +=0        
else :
    bill +=25
    if add_pepperoni == "Y":
        bill +=3
    else:
        bill +=0
    if extra_cheese == "Y":
        bill +=1
    else:
        bill +=0       
print("your total bill is :", bill)        
         
