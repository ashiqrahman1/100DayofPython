import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carmanager = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.createCar()
    carmanager.moveCars()
    for car in carmanager.create_car:
        if car.distance(player) < 21:
            game_is_on = False
            score.gameover()
    # Detect SuccessFull Crossing
    if player.is_finish():
        player.starting_pos()
        score.levelup()
        carmanager.levelup()
screen.exitonclick()
# player.up()
