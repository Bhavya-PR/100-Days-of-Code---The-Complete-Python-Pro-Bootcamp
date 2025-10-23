from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(25 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady= 50 , background="#FFF5F2")

title_label = Label(text="Timer",foreground=GREEN,font=("Times new roman",35,"bold"),background="#FFF5F2")
title_label.grid(row=0,column=1)

canvas = Canvas(width=200, height=223, background="#FFF5F2",highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,111,image = tomato_img)
timer_text = canvas.create_text(101,137,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",foreground="white",background="#568F87",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",foreground="white",background="#568F87",highlightthickness=0)
reset_button.grid(row=2,column=2)

check_marks = Label(text="✓",foreground=GREEN,font=("Arial",25,"bold"),background="#FFF5F2")
check_marks.grid(row=3,column=1)



window.mainloop()
