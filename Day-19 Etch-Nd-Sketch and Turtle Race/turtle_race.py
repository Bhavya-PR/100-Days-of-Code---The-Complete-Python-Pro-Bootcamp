from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 1000 , height = 800)
user_bet = screen.textinput(title = "Make Your Bet", prompt =  "Who will win the race?Enter a colour: ")

colors = ["violet","indigo","blue","green","yellow","orange","red"]
y_value = 400
is_race_on = False
all_turtle = []

if user_bet:
    is_race_on = True

for i in range(0,7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    y_value = y_value - 100
    new_turtle.goto(x = -480, y = y_value)
    all_turtle.append(new_turtle)

while is_race_on:
    for turt in all_turtle:
        turt.speed("fastest")
        if turt.xcor() > 480:
            is_race_on = False
            if turt.pencolor() == user_bet:
                print(f"You've won! The {user_bet} turtle is the winner! ")
            else:
                print(f"You've lost! The {turt.pencolor()} turtle is the winner! ")
        random_distance = random.randint(0,10)
        turt.forward(random_distance)

screen.exitonclick()
