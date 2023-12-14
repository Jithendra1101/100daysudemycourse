import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to slient auction:")

bids = {}
bidingover = False
while True :
    clear_console()
    print("\n **Welcome to biding game** \n")
    name = input("what is your name:")
    bid = int(input("what is your bid: ₹"))
    bids[name] = bid
    bidingover = int(input("\nAre there any other bidders? Type 1 for Yes and  0 for No:"))
    if bidingover == 0:
        break
clear_console()
highestbid = 0  
highestbidder = ""
for bidder in bids:
    if bids[bidder] > highestbid:
        highestbid = bids[bidder]
        highestbidder = bidder
print(f"\n\n\n\nThe winner is {highestbidder} with a bid of ${highestbid}\n\n\n\n\n")
    
    
    
    