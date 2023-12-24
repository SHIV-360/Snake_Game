from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 50, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
