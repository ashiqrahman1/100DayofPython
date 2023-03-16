from turtle import Screen
import time
from snake import Snake
from Food import Food
from score import Score
snake = Snake()
food = Food()
score = Score()
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
is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.snake_shape[0].distance(food) < 15:
        food.refreshfood()
        snake.extent()
        score.update()
        # snake.add_square()
        # screen.update()

    # Detect Collsion with Wall
    if snake.snake_shape[0].xcor() > 280 or snake.snake_shape[0].xcor() < -280 or snake.snake_shape[0].ycor() > 280 or snake.snake_shape[0].ycor() < -280:
        is_game_over = True
        score.game_over()

    for seg in snake.snake_shape[1:]:
        if snake.snake_shape[0].distance(seg) < 10:
            is_game_over = True
            score.game_over()
screen.exitonclick()
