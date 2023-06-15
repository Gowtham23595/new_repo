import turtle
import pandas as pd
from turtle import Screen,Turtle

ALIGNMENT = "left"
FONT = ('Arial', 5, 'normal')

screen = Screen()
screen.title("Us State_games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

us_states_data = pd.read_csv("50_states.csv")
state_list = us_states_data["state"].to_list()
print(us_states_data)



def app():
    game_is_on = True
    def on_cancel():
        game_is_on = False
    count = 0
    while game_is_on:
        user_input = screen.textinput(title="User Input",prompt="Enter the correct states")
        #screen.onclick(,fun=on_cancel)
        if user_input in state_list:
            t = Turtle()
            t.hideturtle()
            t.penup()
            row_data = us_states_data[us_states_data["state"] == user_input]
            print(row_data)
            x = int(row_data["x"])
            y = int(row_data["y"])
            name_of_state = user_input
            print(f"name of state {user_input}")
            t.goto(x,y)
            t.write(f"{name_of_state}",align=ALIGNMENT,font=FONT)
            count +=1
            screen.title(titlestring=f"{count}")
            screen.update()


if __name__=="__main__":
    app()
turtle.mainloop()