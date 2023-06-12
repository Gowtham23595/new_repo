from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=3,stretch_len=1)

    def update_position(self,position):
        self.goto(position)

    def up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(),y_cor+20)

    def down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(),y_cor-20)