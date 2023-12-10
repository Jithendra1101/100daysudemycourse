print("welcome to hights number calculator\n")
number_instring = input("enter the numbers with space in  between : ")
numbers = number_instring.split(" ")
numbers = list(map(int, numbers))
highest = 0
for number in numbers :
    if highest < number :
       highest = number
print("the highest number in the follwing given list is :" , highest)       
    