from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveforward():
    tim.forward(10)


def clockvise():
    tim.right(10)
    # print(tim.pos())


def anticlock():
    tim.left(10)


def back():
    tim.backward(10)


def clear():
    tim.reset()
    # tim.setheading(0)
    tim.clear()


# tim.forward(100)
# tim.setheading(90)
# tim.forward(100)
screen.listen()
screen.onkey(fun=moveforward, key="w")
screen.onkey(fun=clockvise, key="d")
screen.onkey(fun=back, key="s")
screen.onkey(fun=anticlock, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
