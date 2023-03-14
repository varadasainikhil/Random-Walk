import random
import turtle as t
from random import choice
t.colormode(255)
# Setting the number of iterations
iterations = 100

turtle = t.Turtle()
screen = t.Screen()
screen.setup(400, 400)
turtle.shape("arrow")
turtle.speed("fastest")
direction = [0, 90, 180, 270, 360]
turtle.width(5)


for i in range(iterations):
    turtle.setheading(choice(direction))
    turtle.forward(30)
    turtle.pencolor(random.randint(1,255), random.randint(1,255), random.randint(1,255))

screen.exitonclick()

