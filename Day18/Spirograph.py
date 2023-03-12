from turtle import Turtle, Screen

circle = Turtle()
screen = Screen()
circle.speed(10)
# current_heade = circle.heading()
# circle.setheading(current_heade + 10)
for _ in range(100):
    circle.circle(100)
    circle.left(10)
# for i in range(0, 180):
#     circle.circle(50)
#     circle.setheading(circle.heading() + i * 10)
screen.exitonclick()
