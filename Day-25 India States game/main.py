import turtle
import pandas
data = pandas.read_csv("28_states_india.csv")
screen = turtle.Screen()
screen.title("India States Game")

image = "india.gif"
screen.addshape(image)
turtle.shape(image)

states = data.state.to_list()
lowercase_states = [state.lower() for state in states]

is_quiz_on = True
state_guessed = 0
user_guessed_states = []
while is_quiz_on:
    if state_guessed == 28:
        turt = turtle.Turtle()
        turt.write("All States have been Guessed!\nCongratulations!!",align="center",font=("Times New Roman",40,"bold italic"))
        is_quiz_on = False
    else:
        user_answer = screen.textinput(title=f"{state_guessed}/28 State Guessed",prompt="Enter state name :")
        if user_answer.lower() == "exit":
            is_quiz_on = False
        else:
            if user_answer.lower() in lowercase_states:
                state_guessed += 1
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data[data["state"].str.lower() == user_answer.lower()]
                t.goto(state_data.x.item(),state_data.y.item())
                user_guessed_states.append(state_data["state"].item())
                t.write(arg=state_data["state"].item(),align="center",font=("Arial",6,"normal"))
            else:
                print(f"{user_answer} is not present in the states.")
screen.mainloop()

missed_states_by_user = []
for state in states:
    if state not in user_guessed_states:
        missed_states_by_user.append(state)

guess_data = pandas.DataFrame(missed_states_by_user)
guess_data.to_csv("States to Learn.csv")
