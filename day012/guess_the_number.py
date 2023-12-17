import random
print("\n Welcome to guess number game ***\n")
print("\nGuess a number between 1 to 100\n")
#function to return random number 
def randomnumber():
    return random.randint(1,100)
#asking user for the difficulty level eay or hard
attempts = input("\nchoose the difficulty level type: 'easy' or 'hard':")
#assigning number of attemots from the user input
if attempts == "easy":
    attempts = 10
elif attempts == "hard":
    attempts = 5 
else :
    print("invaild input ")
    attempts = 10
#choosing a random number 
random_number = randomnumber()
#printing the number of attemots left for the user to guess the number 
print(f"\n***********you have {attempts} to guess the number ************")

while not attempts == 0:
    guess = int(input("Make a guess:"))
    if guess == random_number:
        print(f"\nYou got it! The answer was {random_number}\n")
        break
    elif guess > random_number:
        print("Too high")
    else:
        print("Too low")
    attempts -= 1
    print(f"\nYou have {attempts} attempts remaining to guess the number")
    if attempts == 0:
        print(f"\nYou've run out of guesses, you lose. The answer was {random_number}")
    


