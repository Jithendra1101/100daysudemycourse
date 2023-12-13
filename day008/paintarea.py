import math
def canscalculator(height,width,cover):
    numscans = (height*width)/cover
    number = math.ceil(numscans)
    print(f"You'll need {number} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
canscalculator(height=test_h, width=test_w, cover=coverage)    