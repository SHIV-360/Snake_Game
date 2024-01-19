from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("score_board.txt", mode="r") as file:
            self.high = int(file.read())  
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.score > self.high:
            self.high = self.score
            with open("score_board.txt", mode="w") as file:
                file.write(str(self.high))

        self.write(f"Score: {self.score}    High Score: {self.high}", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def game_over(self):
        # self.goto(0, 0)
        # self.color("black")
        # self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 50, "normal"))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
