from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        args = "LEVEL : " + str(self.level)
        self.update_screen(args)

    def level_update(self):
        self.level += 1
        args = "LEVEL : " + str(self.level)
        self.update_screen(args)

    def update_screen(self,args):
        self.clear()
        self.write(arg=f"{args}", font=FONT)

    def game_over(self):
        turt = Turtle()
        turt.penup()
        turt.goto(-50, 0)
        turt.hideturtle()
        turt.write(arg="GAME OVER", font=FONT)


