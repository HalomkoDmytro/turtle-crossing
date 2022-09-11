from turtle import Screen
import time
import random

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()

screen.setup(height=600, width=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # finish line
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_score_board()
        manager.update_speed()

    # add car
    if random.randint(1, 6) == 1:
        manager.add_car()

    for car in manager.cars:
        manager.move_forward(car)
        # check collision
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
