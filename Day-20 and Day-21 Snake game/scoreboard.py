from turtle import Turtle
ALIGNMENT = "center"
FONT_TYPE_SCORE = ("Arial", 14, "normal")
FONT_TYPE_GAME = ("Arial", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-2,280)
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT_TYPE_SCORE)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT_TYPE_GAME)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()