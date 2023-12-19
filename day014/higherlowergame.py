from artanddata import logo,vs,data
#importing files
import random

print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b :
      account_b = random.choice(data)

def compare(account_a,account_b):
      if account_a['follower_count'] > account_b['follower_count']:
            return 'A'
      else:
            return 'B'
def formatdata(account):
      name = account['name']
      description = account['description']
      country = account['country']
      return f"{name}, a {description}, from {country}"
  
print("welcome to higher lower game ")
print(formatdata(account_a),"A")
print(vs)
print(formatdata(account_b),"B")
score = 0
game_on = True
while game_on :
      guess = input("who has more followers A or B : ").upper()
      if guess == compare(account_a,account_b):
            score += 1
            print(f"you are right the score is {score}")
            account_a = account_b
            account_b = random.choice(data)
            while account_a == account_b :
                  account_b = random.choice(data)
            print(formatdata(account_a),"A")
            print(vs)
            print(formatdata(account_b),"B")
      else:
            game_on = False
            print(f"you are wrong the score is {score}")
print("thank you for playing game")
