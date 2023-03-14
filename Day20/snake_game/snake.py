from turtle import Turtle
STARTING_POSITION = [(0, 0), (-19, 0), (-39, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_shape = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_shape.append(snake)

    def move(self):
        for number in range(len(self.snake_shape) - 1, 0, -1):
            new_x = self.snake_shape[number - 1].xcor()
            new_y = self.snake_shape[number - 1].ycor()
            self.snake_shape[number].goto(new_x, new_y)
        self.snake_shape[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_shape[0].heading() != DOWN:
            self.snake_shape[0].setheading(UP)

    def down(self):
        if self.snake_shape[0].heading() != UP:
            self.snake_shape[0].setheading(DOWN)

    def left(self):
        if self.snake_shape[0].heading() != RIGHT:
            self.snake_shape[0].setheading(LEFT)

    def right(self):
        if self.snake_shape[0].heading() != LEFT:
            self.snake_shape[0].setheading(RIGHT)
