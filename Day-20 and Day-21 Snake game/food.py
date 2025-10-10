from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.refresh()

    def refresh(self):
        random_x_cord = random.randint(-280,280)
        random_y_cord = random.randint(-280,280)
        self.goto(random_x_cord,random_y_cord)