import os
def espresso(money,water,milk,coffee):
    if money >= 20 :
        if water < 100 or coffee < 18 or milk < 50:
            print("not enough resourses")
        else :   
            water -= 100
            coffee -= 18
            milk   -= 50
            money -= 20
            print("here is your espresso")
    else :
        print("not enough money")
    return(money,water,milk,coffee)
def latte(money,water,milk,coffee):
    if money >= 30 :
        if water < 200 or coffee < 24 or milk < 100:
            print("not enough resourses")
        else :   
            water -= 200
            coffee -= 24
            milk   -= 100
            money -= 30
            print("here is your latte")
    else :
        print("not enough money")
    return(money,water,milk,coffee)

def cappuccino(money,water,milk,coffee):
    if money >= 40 :
        if water < 250 or coffee < 24 or milk < 100:
            print("not enough resourses")
        else :   
            water -= 250
            coffee -= 24
            milk   -= 100
            money -= 40
            print("here is your cappuccino")
    else :
        print("not enough money")
    return(money,water,milk,coffee)

        
def refill(water,milk,coffee):
    water += 1000
    milk   += 1000
    coffee += 200
    print("refilled")
    return(water,milk,coffee)
    
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

coffee_logo = """
  ( (
   ) )
........
|      |]
\      /   
 `----'   
"""
print("welcome to coffee maker")
user_input = input("What would you like? (espresso for 20rs/latte for 15 rs /cappuccino for 15rs): ")
user_input = user_input.lower()
coffee = 200
water = 1000
milk = 600
while not user_input == "off" :
    if user_input == "report" :
        print(f"water: {water}ml")
        print(f"milk: {milk}ml")
        print(f"coffee: {coffee}grams") 
    elif user_input == "refill":
        water,milk,coffee = refill(water,milk,coffee)
        print(f"water: {water}ml")
        print(f"milk: {milk}ml")
        print(f"coffee: {coffee}grams") 
    else :
        money = int(input("how much money do you have "))
        if user_input == "espresso":
          money,water,milk,coffee = espresso(money,water,milk,coffee)
        elif user_input == "latte":
            money,water,milk,coffee = latte(money,water,milk,coffee)    
        elif user_input == "cappuccino":
            money,water,milk,coffee = cappuccino(money,water,milk,coffee)
        else :
            print("invalid input ENTER CORRECT INPUT")
            user_input = input("What would you like? (espresso for 20rs/latte for 15 rs /cappuccino for 15rs): ")      
    print(coffee_logo)
    print(f"here is your blance money :{money}")
    print("\n\n\n\n\n\n\n\n\n\n\n\nwelcome to coffee maker")
    user_input = input("What would you like? (espresso for 20rs/latte for 15 rs /cappuccino for 15rs): ")
print("machine turned off")