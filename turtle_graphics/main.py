import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

my_own_turtle = Turtle()
my_own_turtle.shape("turtle")
my_own_turtle.color("red")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    return random.choice(colors)


# for j in range(3,10):
#     for i in range(j):
#         my_own_turtle.forward(100)
#         my_own_turtle.right(int(360/j))
#     my_own_turtle.pencolor(random_color())

directions = [0,90,180,270]
# my_own_turtle.pensize(15)
my_own_turtle.speed("fastest")
#
# for _ in range(200):
#     my_own_turtle.color(random_color())
#     my_own_turtle.forward(30)
#     my_own_turtle.setheading(random.choice(directions))

for i in range(360):
    my_own_turtle.color(random_color())
    my_own_turtle.setheading(i)
    my_own_turtle.circle(100)


screen = Screen()
screen.exitonclick()
