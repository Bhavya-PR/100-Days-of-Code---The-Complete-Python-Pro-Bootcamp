from tkinter import *

def mile_to_km_calculator():
    mile_value = float(user_input.get())
    km_value = 1.60934 * mile_value
    label3.config(text=str(km_value))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300 , height= 150)
window.config(padx=20,pady=20)

user_input = Entry(width=8)
user_input.grid(row=0,column=1)

label1 = Label(text="Miles",font=("Arial",15,"bold"))
label1.grid(row=0,column=3)

label2 = Label(text="is equal to ",font=("Arial",15,"bold"))
label2.grid(row=1,column=0)

label3 = Label(text='0', font=("Arial",15,"bold"))
label3.grid(row=1,column=1)
label3.config(padx=10)

label4 = Label(text="Km",font=("Arial",15,"bold"))
label4.grid(row=1,column=2)

button = Button(text="Calculate",pady=5,command=mile_to_km_calculator,font=("Arial",15,"italic"))
button.grid(row=2,column=1)

window.mainloop()