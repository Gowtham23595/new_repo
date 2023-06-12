from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.tracer(0)


def app():
    r_paddle = Paddle()
    r_paddle.update_position((350,0))

    l_paddle = Paddle()
    l_paddle.update_position((-340,0))
    screen.listen()
    screen.onkey(r_paddle.up,"Up")
    screen.onkey(r_paddle.down,"Down")
    screen.onkey(l_paddle.up,"w")
    screen.onkey(l_paddle.down,"s")

    ball = Ball()
    score = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()

        #bounce the ball back from when hit top or bottom
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(
                    l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        #detect missed by R
        if ball.xcor() > 380:
            ball.reset()
            score.update_l()

        # detect missed by L
        if ball.xcor() < -380:
            ball.reset()
            score.update_r()

        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    app()

