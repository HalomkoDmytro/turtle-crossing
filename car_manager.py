from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.goto(300, random.randint(-250, 250))
        car.right(180)
        self.cars.append(car)

    def update_speed(self):
        self.move_speed += MOVE_INCREMENT

    def move_forward(self, car):
        car.forward(self.move_speed)
