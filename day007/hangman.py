import random 
#adding words to guess 
word_list = ["apple","orange","banana"]
#chossing of random word from the list of words
guessword = random.choice(word_list)
#adding a display where we show the letter and the poistion of the letter guessed
display = []
length = len(guessword)
for i in range(length):
    display += "_"
print("\n Guess a fruit :\n")
print("\n",display,"\n")
#adding the animation 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#giving chances to the user of 6 lives 
lives = 6
#creating a whiles looop if any character in the display list is empty loop else get out of loop
while "_" in display:
    #taking input of a letter from user and changing the letter to lower case 
    guessed = input("\nGuess a letter: ").lower()
    #taking a for loop in range of the random guessword 
    for postion in range(length):
        letter = guessword[postion]
        if letter == guessed:
            print("\nyour right guess is right \n")
            display[postion] = letter
            print(display)  
    if guessed not in guessword:
        print("\nwrong\n")
        print(stages[lives])
        lives -= 1
        print("\nLives lefts to guess is :",lives,"\n")
    if lives == 0:
        print(" YOU LOST ")
        break
if lives > 0:
    print("you win")