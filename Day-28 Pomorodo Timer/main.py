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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer",foreground=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (1,3,5,7):
        title_label.config(text="Work",foreground=GREEN)
        count_down(work_sec)
    elif reps in (2,4,6):
        title_label.config(text="Break",foreground=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        title_label.config(text="Break",foreground=RED)
        count_down(long_break_sec)
    else:
        return

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 :
        count_sec = "00"
    if count_min == 0 :
        count_min = "00"
    if 9 >= int(count_min) > 0:
        count_min = "0" + str(count_min)
    if 9 >= int(count_sec) > 0:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✓"
        check_marks.config(text=marks)

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

reset_button = Button(text="Reset",foreground="white",background="#568F87",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

check_marks = Label(foreground=GREEN,font=("Arial",25,"bold"),background="#FFF5F2")
check_marks.grid(row=3,column=1)



window.mainloop()
