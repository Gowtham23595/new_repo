

from turtle import Turtle, Screen


STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segments(pos)

    def add_segments(self,position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.segments.append(new)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(x = new_x,y = new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 270 and self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(0)
