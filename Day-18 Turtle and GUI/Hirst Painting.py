# import colorgram
# colors = colorgram.extract('image.jpg',20)
# rgb_values = []
# for color in colors:
#     rgb_value = []
#     colour = color.rgb
#     rgb_value.extend([colour.r,colour.g,colour.b])
#     rgb_values.append(tuple(rgb_value))
# print(rgb_values)
from random import choices
import turtle
import random
turtle.colormode(255)
dom = turtle.Turtle()
colors = [(234, 233, 232), (179, 155, 126), (229, 233, 230), (149, 103, 52), (224, 215, 219), (190, 138, 46), (221, 225, 229), (56, 122, 154), (26, 34, 55), (143, 28, 23), (130, 169, 184), (135, 182, 167), (64, 29, 60), (172, 96, 130), (58, 105, 67), (107, 36, 65), (154, 74, 114), (28, 47, 37), (69, 146, 177), (47, 55, 110)]
dom.speed("fast")
dom.hideturtle()
for i in range(10):
    for j in range(10):
        dom.dot(20, random.choice(colors))
        dom.penup()
        dom.forward(50)
    dom.setpos(tuple([0.00 , dom.pos()[1] + 50.00]))

screen = turtle.Screen()
screen.exitonclick()