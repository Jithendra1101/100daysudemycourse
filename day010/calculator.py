def add(a,b):
    return a+b 
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b

operation =  {
    "+":add,
    "-":subtract ,
    "*":multiply ,
    "/":divide 
}

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    for symbol in operation:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

main()