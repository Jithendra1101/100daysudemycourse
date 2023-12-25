import turtle

def draw_horse():
    screen = turtle.Screen()
    screen.bgcolor("white")

    horse = turtle.Turtle()
    horse.speed(2)

    # Body
    horse.penup()
    horse.goto(-50, -50)
    horse.pendown()
    horse.color("brown")
    horse.begin_fill()
    horse.circle(50)
    horse.end_fill()

    # Head
    horse.penup()
    horse.goto(0, 0)
    horse.pendown()
    horse.color("brown")
    horse.begin_fill()
    horse.circle(30)
    horse.end_fill()

    # Legs
    for _ in range(4):
        horse.penup()
        horse.goto(-25, -50)
        horse.pendown()
        horse.color("brown")
        horse.pensize(15)
        horse.right(90)
        horse.forward(30)

    # Tail
    horse.penup()
    horse.goto(-75, -25)
    horse.pendown()
    horse.color("brown")
    horse.pensize(5)
    horse.left(45)
    horse.forward(20)

    # Mane
    horse.penup()
    horse.goto(0, 20)
    horse.pendown()
    horse.color("black")
    horse.pensize(5)
    horse.right(90)
    horse.forward(20)

    turtle.done()

# Call the draw_horse function to see the result
draw_horse()
