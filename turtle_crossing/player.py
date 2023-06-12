from turtle import Turtle

INITIAL_POSITION = (0,-280)
FORWARD = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.update_position(INITIAL_POSITION)
        self.setheading(90)

    def update_position(self,position):
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + FORWARD
        self.update_position((self.xcor(),new_y))

    def finish(self):
        self.goto(INITIAL_POSITION)

