import random
import turtle as t
from random import choice

t.colormode(255)

# Setting the number of iterations
iterations = 100

turtle = t.Turtle()
screen = t.Screen()
turtle.shape("arrow")
turtle.speed("fastest")
direction = [0, 90, 180, 270, 360]
turtle.width(5)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


for i in range(iterations):
    turtle.setheading(choice(direction))
    turtle.forward(30)
    turtle.pencolor(random_color())

screen.exitonclick()
