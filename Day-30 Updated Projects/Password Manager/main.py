from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json

# UI setup
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day-30 Updated Projects/Password Manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Functions

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
            new_data = {
                 website:{
                      "Email" : email,
                      "Password" : password
                 }
            }
            try:
                with open("Day-30 Updated Projects/Password Manager/data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("Day-30 Updated Projects/Password Manager/data.json", "w") as data_file:
                    json.dump(
                        new_data,data_file,indent=2
                    )
            else:
                data.update(new_data)
                with open("Day-30 Updated Projects/Password Manager/data.json", "w") as data_file:
                    json.dump(
                        data,data_file,indent=2
                    )
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_entry.delete(0,END)
                email_entry.insert(0,"bhavyapandurangan494@gmail.com")

def search():
    website = website_entry.get()
    try:
        with open("Day-30 Updated Projects/Password Manager/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"Email: {data[website]['Email']}\nPassword: {data[website]['Password']}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for the {website} exists.")

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0,"bhavyapandurangan494@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
search_button = Button(text="Search",width=15,command=search)
search_button.grid(row=1,column=2)
password_button = Button(text="Generate Password",command=password_generator)
password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=38,command=save)
add_button.grid(row=4,column=1,columnspan = 2)

window.mainloop()
