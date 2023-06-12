#main code for snake game
from turtle import Turtle, Screen
import random
from time import time, sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.title(titlestring="My Snake Game")
screen.bgcolor("black")

screen.tracer(0)
screen.listen()


def app():

    game_is_on = True

    # Create a snake
    my_snake = Snake()
    my_food = Food()
    my_score = ScoreBoard()


    screen.update()
    screen.onkey(my_snake.up, "Up")
    screen.onkey(my_snake.down, "Down")
    screen.onkey(my_snake.left, "Left")
    screen.onkey(my_snake.right, "Right")

    while game_is_on:
        #move the snake
        screen.update()
        sleep(0.1)


        if my_snake.head.distance(my_food) < 15:
            my_food.refresh()
            my_snake.extend()
            my_score.update_score()

        x = my_snake.head.xcor()
        y = my_snake.head.ycor()

        if x > 290 or x < -290 or y < -290 or y > 290:
            game_is_on = False
            my_score.game_over_sequence()

        #Check for tail collisions
        for segment in my_snake.segments[1:]:
            if my_snake.head.distance(segment) < 10:
                game_is_on = False
                my_score.game_over_sequence()

        my_snake.move()


if __name__ == "__main__":
    app()


screen.exitonclick()