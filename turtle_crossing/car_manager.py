from turtle import Turtle
import random


colors = ["red","green","yellow","purple","blue","orange"]
STARTING_MOVE_DISTANCE: int = 5
MOVE_INCREMENT = 10
START_POSITION_Y = (-280,280)
START_POSITION_X = 280


class Carmanager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.x_update_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_int = random.randint(0,6)
        if random_int == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            y_pos = random.randint(-250, 250)
            new_car.goto(START_POSITION_X, y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.x_update_distance)

    def update_level(self):
        self.x_update_distance += MOVE_INCREMENT
