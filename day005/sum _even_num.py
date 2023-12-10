print("welcome to sum of numbers calculator")
firstnum = int(input("enter the start number:"))
seconnum = int(input("enter the end number:"))
total = 0
for i in range(firstnum,seconnum + 1):
    if i % 2 == 0 :
        total += i
print("the sum of even numbers is :",total)        
        