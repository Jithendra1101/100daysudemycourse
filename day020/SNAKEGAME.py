from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for segment in segments:
        segment.forward(20)
    
    
    
screen.exitonclick()   


# segment1 = Turtle("square")
# segment1.color("white")

# segment2 = Turtle("square")
# segment2.color("white")
# segment2.goto(-20,0)

# segment3 = Turtle("square")
# segment3.color("white")
# segment3.goto(-40,0)








