from turtle import Turtle, Screen
import random
new_turtle = Turtle()

color = ["red", "green", "blue"]


def draw_shape(number):
    angle = 360 / number
    for _ in range(number):
        new_turtle.forward(100)
        new_turtle.right(angle)


for shape in range(3, 11):
    new_turtle.color(random.choice(color))
    draw_shape(shape)

screen = Screen()
screen.exitonclick()
