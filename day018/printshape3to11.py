from turtle import Turtle , Screen

tut = Turtle()
tut.shape("turtle")
tut.color("orange")

def drawshape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tut.forward(100)
        tut.right(angle)
        
for i in range(3,11):
    drawshape(i)








screen = Screen()
screen.exitonclick()