from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

def button_clicked():
    text = input.get()
    my_label["text"] = text

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text = "Click me", command=button_clicked)
button.grid(column=1, row=1)
button_too = Button(text = "Click me too", command=button_clicked)
button_too.grid(column=2, row=0)

# Entry

input = Entry(width=12)
input.grid(column=3, row=2)


window.mainloop()
