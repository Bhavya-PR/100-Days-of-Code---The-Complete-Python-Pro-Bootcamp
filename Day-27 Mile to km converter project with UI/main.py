import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500 , height=300)

# Label

my_label = tkinter.Label(text= "I am a label.", font=("Arial",24,"italic bold"))
my_label.pack()

my_label["text"] = "Bhavya Pandurangan"
my_label.config(foreground="red")

# Button
def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input,fg="blue")

my_button = tkinter.Button(text="Click me" , command=button_clicked)
my_button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()

# Text
text = tkinter.Text()
text.focus()
text.insert(tkinter.END,"Hello all")
text.pack()

window.mainloop()
