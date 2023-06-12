from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_position = 10
        self.y_position = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor()+self.x_position
        y_cor = self.ycor()+self.y_position
        self.goto(x_cor,y_cor)

    def bounce_y(self):
        self.y_position *= -1

    def bounce_x(self):
        self.x_position *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.x_position *= -1
        self.move_speed = 0.1
