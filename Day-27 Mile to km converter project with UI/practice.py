from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500 , height=300)

# Label

my_label = Label(text= "I am a label.", font=("Arial",24,"italic bold"))
my_label.pack()

my_label["text"] = "Bhavya Pandurangan"
my_label.config(foreground="red")

# Button
def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input,fg="blue")

my_button = Button(text="Click me" , command=button_clicked)
my_button.pack()

# Entry
input = Entry(width=10)
input.pack()

# Text
text = Text(height=5 , width= 30)
text.focus()
text.insert(END,"Hello all")
print(text.get("1.0",END))
text.pack()

# Spinbox
def spinbox_changed():
    print(spinbox.get())
spinbox = Spinbox(from_= 1 , to= 10, width= 2, command=spinbox_changed)
spinbox.pack()

# Scale
def scale_changed(value):
    print(value)
scale = Scale(from_= 20, to= 50, command=scale_changed)
scale.pack()

# Check Box
def checkedstate():
    print(checked_state.get())
checked_state = IntVar()
check_box = Checkbutton(text="Is on?",variable=checked_state,command=checkedstate)
check_box.pack()

# Radio Button
def radio_value():
    print(radio_state.get())
radio_state = Variable()
radio_button_1 = Radiobutton(text="Maths", value="Maths", variable=radio_state,command=radio_value)
radio_button_2 = Radiobutton(text="Chemistry", value="Chemistry", variable=radio_state, command=radio_value)
radio_button_1.pack()
radio_button_2.pack()

# List box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=5)
actors = ["Vijay","SK","Soori","Adharvaa","Mohanlal"]
for actor in actors:
    listbox.insert(actors.index(actor),actor)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()
