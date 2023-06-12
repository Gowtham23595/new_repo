from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}",align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(f"{self.r_score}",align=ALIGNMENT,font=FONT)

    def update_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_l(self):
        self.l_score += 1
        self.update_scoreboard()


