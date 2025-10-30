from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip

# UI setup
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
# Password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    password_entry.delete(0,END)
    letters_list = [(choice(letters)) for i in range(randint(8,10))]
    symbols_list = [(choice(symbols)) for i in range(randint(2,4))]
    numbers_list = [(choice(numbers)) for i in range(randint(2,4))]
    password_list = letters_list+symbols_list+numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# Functions
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) < 1 or len(password) < 1 :
            messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details you entered:"
                                                                 f"\nEmail: {email}\nPassword: {password}"
                                                                 f"\nIs it ok to save?")

        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {password} \n")
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    email_entry.delete(0,END)
    email_entry.insert(0,"bhavyapandurangan494@gmail.com")

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0,"bhavyapandurangan494@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
password_button = Button(text="Generate Password",command=password_generator)
password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=38,command=save)
add_button.grid(row=4,column=1,columnspan = 2)


window.mainloop()
