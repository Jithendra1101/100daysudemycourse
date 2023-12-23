from turtle import Turtle,Screen
import random
length = [10,20,15,5,25,27,22,11,4]
direction = [0,90,180,270]
screen = Screen()

mouse = Turtle()
mouse.shape("turtle")
mouse.color("black")
mouse.speed("fastest")
def randomwalk():
    diretion_choice = random.choice(direction)
    length_choice = random.choice(length)
    mouse.forward(length_choice)
    mouse.right(diretion_choice)

numberoftimes = int(input("How many times do you want to walk? "))
for _ in range(numberoftimes):
    randomwalk()
    
screen.exitonclick()