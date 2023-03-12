from turtle import Turtle, Screen
import random
new_turtle = Turtle()


# new_turtle.color('red', 'yellow')
# new_turtle.begin_fill()
# while True:
#     new_turtle.forward(250)
#     new_turtle.left(170)
#     if abs(new_turtle.pos()) < 1:
#         break
# new_turtle.end_fill()

# new_turtle.forward(200)
# new_turtle.right(90)
# new_turtle.forward(200)
# new_turtle.right(90)
# new_turtle.forward(200)
# new_turtle.right(90)
# new_turtle.forward(200)

# def square():
#     for i in range(4):
#         new_turtle.right(90)
#         new_turtle.forward(200)


# square()

def DashLine():
    for i in range(15):
        new_turtle.forward(10)
        new_turtle.penup()
        new_turtle.forward(10)
        new_turtle.pendown()

# 360 / 4 = 90
# 360 / 5 = 72


# DashLine()
screen = Screen()
screen.exitonclick()
