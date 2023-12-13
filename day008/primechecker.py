import math
def primechecker(number):
    for i in range(2,math.ceil(number/2)):
        if number%i==0:
            print(f"the given number {number} is not a prime number")
            break
        else:
            print(f"the given number {number} is a prime number")
            break

number=int(input("Enter the numberto check prime or not : "))       
primechecker(number)