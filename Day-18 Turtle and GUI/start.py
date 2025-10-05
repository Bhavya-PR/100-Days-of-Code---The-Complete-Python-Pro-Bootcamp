from turtle import Turtle, Screen
import random
dommy = Turtle()
#dommy.shape("turtle")

# Drawing the square using dashed lines
# for i in range(4):
#     j = 0
#     while j < 20:
#         dommy.forward(5)
#         dommy.penup()
#         dommy.forward(5)
#         dommy.pendown()
#         j += 1
#     dommy.right(90)

# Drawing different  shapes
# for i in range(3,11):
#     for j in range(i):
#         dommy.pensize(5)
#         R = random.random()
#         G = random.random()
#         B = random.random()
#         dommy.color(R,G,B)
#         dommy.forward(100)
#         dommy.right(360/i)

# Performing Random Walk
# directions = [0, 90, 180, 270]
# count = 0
# dommy.pensize(5)
# dommy.speed("fastest")
# while count < 101:
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     dommy.color(R,G,B)
#     dommy.setheading(random.choice(directions))
#     dommy.forward(20)
#     count += 1

screen = Screen()
screen.exitonclick()

# import heroes, villains
# print(heroes.gen())
# print(villains.gen())
