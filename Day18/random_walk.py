from turtle import Turtle, Screen
import random

color = ["red", "green", "blue"]
# Turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.speed(10)
tim.pensize(10)
direction = [0, 90, 180, 270]


def random_walk():
    tim.color(random.choice(color))
    tim.setheading(random.choice(direction))
    tim.forward(50)


while True:
    random_walk()
screen.exitonclick()
