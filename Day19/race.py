from turtle import Turtle, Screen
import random
# t2 = Turtle()
# t3 = Turtle()
# t4 = Turtle()
# t5 = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
user_inp = screen.textinput(
    "make you bet", "which Turble will win the Race ? Enter the Color")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]
all_turtle = []
for i in range(0, 6):
    t1 = Turtle()
    t1.shape('turtle')
    t1.penup()
    t1.color(color[i])
    t1.goto(x=-230, y=y_pos[i])
    all_turtle.append(t1)
is_race = False
if user_inp:
    is_race = True
winner = ""
while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            is_race = False
        rand = random.randint(0, 10)
        turtle.forward(rand)

if user_inp == winner:
    print(f"Your are right {winner} is the Winner")
else:
    print(f"You are wrong {winner} is the Winner")
# t2.penup()
# t2.shape('turtle')
# t2.color(random.choice(color))
# t2.goto(x=-230, y=-60)

# t3.penup()
# t3.shape('turtle')
# t3.color(random.choice(color))
# t3.goto(x=-230, y=-20)

# t4.penup()
# t4.shape('turtle')
# t4.color(random.choice(color))
# t4.goto(x=-230, y=20)

# t5.penup()
# t5.shape('turtle')
# t5.color(random.choice(color))
# t5.goto(x=-230, y=60)
# # create object based on number
# for i in range(number):

screen.exitonclick()
