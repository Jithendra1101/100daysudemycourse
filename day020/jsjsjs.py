import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Simple Mario Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Mario character
mario = turtle.Turtle()
mario.shape("square")
mario.color("red")
mario.shapesize(stretch_wid=1, stretch_len=2)
mario.penup()
mario.goto(-300, -250)

# Ground
ground = turtle.Turtle()
ground.shape("square")
ground.color("green")
ground.shapesize(stretch_wid=1, stretch_len=40)
ground.penup()
ground.goto(0, -300)

# Platforms
platforms = []
for _ in range(5):
    platform = turtle.Turtle()
    platform.shape("square")
    platform.color("brown")
    platform.shapesize(stretch_wid=1, stretch_len=4)
    platform.penup()
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    platform.goto(x, y)
    platforms.append(platform)

# Gravity
gravity = -0.5
mario_speed = 0

# Jumping
def jump():
    global mario_speed
    if mario.ycor() == -250:
        mario_speed = 10

# Keyboard bindings
screen.listen()
screen.onkey(jump, "space")

# Main game loop
while True:
    screen.update()

    # Move Mario
    mario_speed += gravity
    mario.sety(mario.ycor() + mario_speed)

    # Check for collision with ground
    if mario.ycor() < -250:
        mario_speed = 0
        mario.sety(-250)

    # Check for collision with platforms
    for platform in platforms:
        if (mario.xcor() - 20 < platform.xcor() < mario.xcor() + 20) and (mario.ycor() - 20 < platform.ycor() < mario.ycor() + 20):
            mario_speed = 0
            mario.sety(platform.ycor() + 20)

    # Move platforms
    for platform in platforms:
        platform.setx(platform.xcor() - 1)

        # Respawn platform if it goes off-screen
        if platform.xcor() < -400:
            platform.goto(400, random.randint(-200, 200))
