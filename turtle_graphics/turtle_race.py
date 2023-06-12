from turtle import Turtle, Screen
import random

def app():

    screen = Screen()
    screen.setup(width=500, height=400)
    # Get input from the user
    user_bet = screen.textinput(title="Enter color", prompt="Which turtle will win?")
    color_list = ["red", "blue", "green", "yellow", "orange", "brown"]
    turtle_list = []
    y_pos = [-70, -40, -10, 20, 50, 80]

    for turtle_index in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color_list[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x = -230,y=y_pos[turtle_index])
        turtle_list.append(new_turtle)

    race_is_on = True
    while race_is_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                race_is_on = False
                if user_bet == turtle.pencolor():
                    print(f"You won,{user_bet} wins the race")
                else:
                    print(f"You lose, {turtle.pencolor()} wins the race")
            turtle.forward(random.randint(0,10))
    screen.exitonclick()


if __name__ == "__main__":
    app()




