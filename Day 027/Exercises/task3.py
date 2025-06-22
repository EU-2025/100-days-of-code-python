from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    text = input.get()
    my_label["text"] = text

button = Button(text = "Click me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=12)
input.pack()



window.mainloop()
