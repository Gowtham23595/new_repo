import random
import turtle
import colorgram
from turtle import Turtle, Screen


turtle.colormode(255)
naruto = Turtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
              (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))

print(color_list)

naruto.setheading(225)
naruto.penup()
naruto.forward(320)
naruto.setheading(0)
naruto.speed("fastest")
naruto.hideturtle()
def draw_dots():
    for _ in range(10):
        naruto.dot(20,random.choice(color_list))
        naruto.forward(50)

def draw_rows():

    for _ in range(10):
        draw_dots()
        naruto.setheading(90)
        naruto.forward(50)
        naruto.setheading(180)
        naruto.forward(500)
        naruto.setheading(0)



draw_rows()

screen = Screen()
screen.exitonclick()


