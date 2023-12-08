print("  ********* BMI CALCULATOR ********")
height=input("enter your height in centimeters: ")
weight=input("enter your weight in kg: ")
bmi=float((int(weight)/float(height)**2)*10000)
print("your bmi is ",bmi,)
if bmi<18.5:
    print("you are underweight")
elif bmi>18.5 and bmi<=25:
     print("you are normaL")
elif bmi>=26 and bmi<30:
    print("you are over weight")
else:
    print("you have obesity")