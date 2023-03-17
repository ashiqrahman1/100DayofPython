from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.create_car = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        rand_num = random.randint(1, 6)
        if rand_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-220, 220)
            new_car.goto(300, rand_y)
            self.create_car.append(new_car)

    def moveCars(self):
        for move in self.create_car:
            move.backward(STARTING_MOVE_DISTANCE)

    def levelup(self):
        self.carspeed += MOVE_INCREMENT
