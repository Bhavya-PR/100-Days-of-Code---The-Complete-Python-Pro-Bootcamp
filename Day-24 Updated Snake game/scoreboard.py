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
        with open("Day-24 Updated Snake game/data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT_TYPE_SCORE)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day-24 Updated Snake game/data.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()