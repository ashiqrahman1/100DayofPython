from turtle import Turtle, Screen
import time
from snake import Snake
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
# setting background color
screen.bgcolor("black")
screen.title("Welcome")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
# snake_shape = []
# # snake shape
# for i in range(3):
#     snake = Turtle()
#     snake.shape("square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(i * -19, 0)
#     snake_shape.append(snake)

# while True:
#     screen.update()
#     time.sleep(0.1)
#     for numb in range(len(snake_shape)-1, 0, -1):
#         new_x = snake_shape[numb - 1].xcor()
#         new_y = snake_shape[numb - 1].ycor()
#         snake_shape[numb].goto(new_x, new_y)
#     snake_shape[0].forward(20)
#     snake_shape[0].left(90)


screen.exitonclick()
