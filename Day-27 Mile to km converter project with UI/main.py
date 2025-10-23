from tkinter import *

def button_clicked():
    user_choice = user_input.get()
    label.config(text=user_choice)

window = Tk()
window.title("GUI")
window.minsize(width=300 , height= 500)
window.config(padx=20,pady=100)

# Label
label = Label(text="I am a Label" , font=("Arial",15,"bold"))
# label.pack()
# label.place(x = 20 , y = 40)
label.grid(row=0,column=0)
label.config(padx=100,pady=100)

# Button
button = Button(text="Submit",command=button_clicked)
# button.pack()
# button.place(x = 20 , y = 70)
button.grid(row=1,column=1)

# Entry
user_input = Entry(width=15)
print(user_input.get())
# user_input.pack()
user_input.grid(row=2,column=3)

# New Button
button_2 = Button(text="New Button")
button_2.grid(row=0,column=2)

window.mainloop()