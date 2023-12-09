print("\nWelocme to random name genaretor\n")
names_string = input("Enter names seprated by comma ' , ' :")
names = names_string.split(",")
import random
nameslen = len(names)
bill_payer = random.randint(0,nameslen-1)
print("The random person is :" , names[bill_payer])
