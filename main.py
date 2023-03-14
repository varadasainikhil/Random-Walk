from turtle import Turtle, Screen
from random import choice

# Setting the number of iterations
iterations = 100

turtle = Turtle()
screen = Screen()
screen.setup(400, 400)
turtle.shape("arrow")
turtle.speed("fastest")
color = ["red", "blue", "yellow", "black", "orange", "purple", "brown", "pink"]
direction = [0, 90, 180, 270, 360]
turtle.width(5)

for i in range(iterations):
    turtle.setheading(choice(direction))
    turtle.forward(30)
    turtle.color(choice(color))

screen.exitonclick()

