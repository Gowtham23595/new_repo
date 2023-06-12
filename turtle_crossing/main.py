from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Carmanager

import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title(titlestring="Turtle Crossing")

screen.tracer(0)


def app():

    game_is_on = True
    my_player = Player()
    score = Scoreboard()

    screen.listen()
    screen.onkey(my_player.move_up,"Up")

    count = 0
    car_list = []
    car_manager = Carmanager()

    while game_is_on:
        time.sleep(0.1)

        car_manager.create_cars()
        car_manager.move_cars()

        if my_player.ycor() > 280:
            my_player.finish()
            score.update_level()
            car_manager.update_level()

        for car in car_manager.all_cars:
            if car.distance(my_player) < 20:
                game_is_on = False
                score.game_over()

        screen.update()
        count += 1
    screen.exitonclick()

if __name__=="__main__":
    app()