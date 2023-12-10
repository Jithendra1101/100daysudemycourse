print("\nwelocme to height calcuator\n")
heightsin = input("enter the heights of each students with a space in between :")

heights = heightsin.split(" ")
length = len(heights)
heights = (int(height) for height in heights)
sum  = sum(heights)
avg = sum / (length)    
print ("avrage of all the heights is ",avg)